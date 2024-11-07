import boto3
import botocore.config
import json
import logging
from botocore.exceptions import ClientError

# Configure global logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Initialize AWS SDK clients outside the handler to reuse connections
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print("ENtered the function")
    logger.info("Lambda function invoked.")

    # Check if 'Records' exist in the event
    if 'Records' not in event:
        logger.error("No records found in the event.")
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid event format: No records found.')
        }

    try:
        # Get the bucket and file name from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        input_file_key = event['Records'][0]['s3']['object']['key']
        logger.debug(f"Bucket name: {bucket_name}")
        logger.debug(f"File key: {input_file_key}")
        print("Bucket success")
        print("File present in the event:", event['Records'][0]['s3']['object']['key'])


        logger.info("Successfully retrieved bucket and key information from the event.")
    except KeyError as e:
        logger.error(f'Error reading event details: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error reading event details: {str(e)}')
        }
    
    try:
        # Step 1: Read the file from S3
        print("ENtered the reading of S3")
        response = s3_client.get_object(Bucket=bucket_name, Key=input_file_key)
        if 'Body' not in response:
            raise Exception("Missing 'Body' in S3 response.")
        file_content = response['Body'].read().decode('utf-8')  # Assuming the content is text
        print("ENtered the file_content")
        logger.info("File content read successfully from S3.")
    except ClientError as e:
        logger.error(f'Error reading from S3: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error reading from S3: {str(e)}')
        }
    except Exception as e:
        logger.error(f'Unexpected error while reading S3: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Unexpected error while reading S3: {str(e)}')
        }
    
    # Step 2: Construct the prompt for the Bedrock model
    prompt = f"""You are an expert script annotator. Your task is to label the provided movie script according to specific categories to enhance clarity and organization. Label the script using the following guidelines:

**[DESCRIPTION: ...]** - Use this label for general descriptions of the narrative, character states, and emotional context.

**[SCENE HEADING: ...]** - Use this label for the headings that indicate the setting and time of the scene. These usually start with EXT. (exterior) or INT. (interior), followed by the location and time of day.

**[CHARACTER INTRODUCTION: ...]** - Use this label to mark the introduction of important characters in the scene.

**[CHARACTER: ...]** - Use this label to identify the character speaking in the dialogue that follows.

**[LINE: ...]** - Use this label for the actual dialogue spoken by the character.

**[TRANSITION: ...]** - Use this label for any scene transitions, such as "FADE OUT," "FADE IN," or "CUT TO."

Please label the provided script in this manner, ensuring that you maintain the structure and clarity. If there are any sections where you are uncertain about how to label, do not provide any label for those sections. Instead, indicate your uncertainty by stating, "Uncertain about labeling."

"""
    print("ENtered the prompt")

    # Step 3: Call the Bedrock model with the prompt
    try:
        body = {
            "prompt":prompt,
            "max_tokens":800,
            "temperature":0.5,
            "top_p":0.9,
            "top_k":50
        }
        print("ENtered the invoke model")
        bedrock_client = boto3.client("bedrock-runtime", region_name="eu-west-2", config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 2}))

        response = bedrock_client.invoke_model(body=json.dumps(body), modelId="mistral.mistral-7b-instruct-v0:2", contentType= "application/json",accept= "application/json", # Ensure this model ID is correct
        )
        print(response)
        
        #if 'Body' not in response:
            #raise Exception("Missing 'Body' in Bedrock response.")
        
        response_content = response.get('body').read()
        response_data = json.loads(response_content)
        print(response_data)
        logger.info(f"Response from model: {response_data}")

        output = response_data.get('generation', 'No generation found in response.')

        return {
            'statusCode': 200,
            'body': json.dumps(output)
        }

    except ClientError as e:
        logger.error(f"Client error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Client error: {str(e)}")
        }
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Unexpected error: {str(e)}")
        }
