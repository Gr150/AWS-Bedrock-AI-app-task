import json
import xml.etree.ElementTree as ET
import boto3
import logging
import base64
import os

# Set up AWS clients and logging
lambda_client = boto3.client('lambda')
s3_client = boto3.client('s3')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configuration constants
BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'storyfyscripts')
S3_KEY = 'uploaded_script.fdx'
OUTPUT_KEY = 'converted_file.json'
LAMBDA_FUNCTION_ARN = os.getenv('LAMBDA_FUNCTION_ARN', 'arn:aws:lambda:eu-west-2:039612872581:function:script_evaluator')

def upload_to_s3(bucket, key, body, content_type):
    """Upload a file to S3."""
    try:
        s3_client.put_object(Bucket=bucket, Key=key, Body=body, ContentType=content_type)
        logger.info(f"File uploaded to S3: {bucket}/{key}")
    except Exception as e:
        logger.error(f"Failed to upload file to S3: {e}")
        raise

def remove_script_notes(element):
    """Recursively remove all <ScriptNote> elements from the XML tree."""
    for script_note in element.findall(".//ScriptNote"):
        parent = script_note.getparent()
        if parent is not None:
            parent.remove(script_note)

def parse_xml_content(xml_content):
    """Parse and process XML content, removing <ScriptNote> elements."""
    try:
        root = ET.fromstring(xml_content)
        remove_script_notes(root)
        return root
    except ET.ParseError as e:
        logger.error("Failed to parse XML content", exc_info=True)
        raise ValueError("Invalid XML content")

def collect_script_content(element, level=0):
    """Recursively collect content from an XML element, post-processing."""
    content = []
    text = (element.text or '').strip()
    
    if text:
        content.append(f"{'  ' * level}{text}")

    for child in element:
        content.extend(collect_script_content(child, level + 1))

    return content

def invoke_lambda_function(payload):
    """Invoke a Lambda function and return the response."""
    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_ARN,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        return json.load(response['Payload'])
    except Exception as e:
        logger.error("Failed to invoke Lambda function", exc_info=True)
        raise

def lambda_handler(event, context):
    try:
        # Validate and decode the incoming base64 file content
        if 'body' not in event:
            raise ValueError("Missing 'body' in event")

        file_content = base64.b64decode(event['body'])
        
        # Upload the original file to S3
        upload_to_s3(BUCKET_NAME, S3_KEY, file_content, 'application/xml')

        # Parse and process the XML content
        root = parse_xml_content(file_content.decode('utf-8'))
        script_content = collect_script_content(root)

        # Convert to JSON format
        script_data = {"content": script_content}
        json_content = json.dumps(script_data, indent=4)

        # Upload the JSON result to S3
        upload_to_s3(BUCKET_NAME, OUTPUT_KEY, json_content, 'application/json')

        # Invoke another Lambda with the JSON content
        response_from_master = invoke_lambda_function(script_data)

        return {
            'statusCode': 200,
            'body': json.dumps(response_from_master)
        }

    except ValueError as e:
        logger.error("Input validation or processing error", exc_info=True)
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        logger.error("An unexpected error occurred", exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': "Internal server error"})
        }
