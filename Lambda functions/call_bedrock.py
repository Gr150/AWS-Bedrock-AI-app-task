import boto3
import botocore.config
import json
import logging
from botocore.exceptions import ClientError
import time

# Configure global logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Global Bedrock client configuration
bedrock_client_config = botocore.config.Config(read_timeout=300, retries={'max_attempts': 2})

def lambda_handler(event, context):
    # If event is a single dictionary, wrap it in a list for unified processing
    events = event if isinstance(event, list) else [event]
    
    # Loop through events and process each
    for single_event in events:
        data = single_event.get('data')
        prompt = single_event.get('prompt')
        function_name = single_event.get('function_name')
        
        logger.info(f"Processing prompt for function: {function_name}")
        
        # Call models
        response_claude = call_model("ap-south-1", "anthropic.claude-3-sonnet-20240229-v1:0", prompt, function_name, model_prefix="claude")
        response_mistral = call_model("eu-west-2", "mistral.mistral-7b-instruct-v0:2", prompt, function_name, model_prefix="mistral")
        # Uncomment to add Llama if needed
        # response_llama = call_model("eu-west-2", "llama.model-id", prompt, function_name, model_prefix="llama")

        # Delay between processing each event if necessary
        time.sleep(6)

    return {"status": "processing complete"}

def call_model(region, model_id, prompt, function_name, model_prefix):
    try:
        # Initialize Bedrock client only once per model call
        bedrock_client = boto3.client("bedrock-runtime", region_name=region, config=bedrock_client_config)
        
        # Model request payload
        body = json.dumps({
            "prompt": prompt,
            "max_tokens": 600,
            "temperature": 0.5,
            "top_p": 0.9,
            "top_k": 50
        })

        logger.info(f"Calling model {model_id} in {region} for {function_name}")

        # Invoke the model
        response = bedrock_client.invoke_model(
            body=body,
            modelId=model_id,
            contentType="application/json",
            accept="application/json"
        )

        # Process and save response
        response_data = json.loads(response['body'].read())
        if response_data:
            s3_key = f"{function_name}_{model_prefix}.txt"
            save_response_s3(s3_key, "storifyresponse", response_data)
        
        return response_data

    except ClientError as e:
        logger.error(f"ClientError calling model {model_id}: {e}")
    except Exception as e:
        logger.error(f"Error calling model {model_id}: {e}")
        return {"error": str(e)}

def save_response_s3(s3_key, s3_bucket, response_data):
    s3 = boto3.client('s3')
    try:
        # Save response to S3
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=json.dumps(response_data))
        logger.info(f"Response saved to S3: {s3_key}")
    except Exception as e:
        logger.error(f"Error saving response to S3: {e}")
