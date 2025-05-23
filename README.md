# AWS-Bedrock-AI-app-task

## Overview

This project showcases how to integrate AWS Bedrock's AI capabilities into a serverless application. The app allows users to upload screenplay files, extract meaningful content, and generate summaries using AI models via AWS Bedrock.

It uses AWS Lambda, API Gateway, and Amazon S3 for a fully serverless, scalable solution.

## Features

- 📄 Upload screenplay files (`.fdx` format)
- ✂️ Extract relevant content using Lambda
- 🤖 Generate AI-based summaries using AWS Bedrock
- ⚙️ Serverless deployment via AWS SAM
- ☁️ Scalable architecture using AWS services

## Architecture

![Architecture Diagram](architecture%20diagram.png)

1. **API Gateway** – Accepts user file uploads and summary requests  
2. **AWS Lambda** – Handles file processing and calls AWS Bedrock  
3. **Amazon S3** – Stores raw files and processed content  
4. **AWS Bedrock** – Generates summaries using foundation models

## Getting Started

### Prerequisites

- AWS Account with Bedrock access
- AWS CLI configured
- AWS SAM CLI installed
- Python 3.8 or newer

### Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/Gr150/AWS-Bedrock-AI-app-task.git
   cd AWS-Bedrock-AI-app-task
