Overview
This project demonstrates the integration of AWS Bedrock's AI capabilities into a serverless application. The application processes user-uploaded screenplay files, extracts meaningful content, and generates summaries using AI models. It leverages AWS services such as Lambda, S3, and API Gateway to create a scalable and efficient workflow.

Features
File Upload: Users can upload screenplay files (e.g., .fdx format) to the application.

Content Extraction: The application parses the uploaded files to extract relevant content.

AI Summarization: Utilizes AWS Bedrock to generate summaries of the extracted content.

Serverless Architecture: Built using AWS Lambda functions and managed via AWS SAM (Serverless Application Model).

Scalable and Efficient: Designed to handle multiple requests with minimal latency.

Architecture

The application follows a serverless architecture:

API Gateway: Serves as the entry point for file uploads and summary requests.

AWS Lambda: Handles file processing, content extraction, and interaction with AWS Bedrock.

Amazon S3: Stores uploaded files and processed outputs.

AWS Bedrock: Provides AI capabilities for content summarization.

Getting Started
Prerequisites
AWS Account with appropriate permissions.

AWS CLI configured on your local machine.

AWS SAM CLI installed.

Python 3.8 or higher.

Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/Gr150/AWS-Bedrock-AI-app-task.git
cd AWS-Bedrock-AI-app-task
Build the Application:

bash
Copy
Edit
sam build
Deploy the Application:

bash
Copy
Edit
sam deploy --guided
Follow the prompts to set up your stack name, AWS region, and other configurations.

Usage
Upload a Screenplay File:

Use the provided API endpoint to upload a .fdx file.

Generate Summary:

After uploading, invoke the summary endpoint to receive an AI-generated summary of the screenplay.

Project Structure
Lambda functions/: Contains the AWS Lambda function code.

scriptify template.yaml: AWS SAM template defining the application's infrastructure.

architecture diagram.png: Visual representation of the application's architecture.

sample_script.fdx: Sample screenplay file for testing.

converted_file.json: Example of extracted content from a screenplay.

README.md: This file.

Scriptify App Documentation.pdf: Detailed documentation of the application.

Technical Challenge 3Gi.pdf: Original technical challenge description.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

License
This project is licensed under the MIT License.
