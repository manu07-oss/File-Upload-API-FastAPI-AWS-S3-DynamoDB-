# File-Upload-API-FastAPI-AWS-S3-DynamoDB
🎯 What this demonstrates
REST API design (using FastAPI)
AWS SDK usage (boto3)
Clean code + modular structure
Error handling + production mindset
📌 Use Case

A simple service where:

User uploads a file (image, PDF, etc.)
File is stored in S3
Metadata (file name, size, upload time) is stored in DynamoDB
Architecture Flow
Client → FastAPI → S3 (file storage)
                  → DynamoDB (metadata)

Project Structure
file-upload-api/
│── app.py
│── aws/
│    ├── s3.py
│    ├── dynamodb.py
│── models.py
│── requirements.txt


requirements.txt
fastapi
uvicorn
boto3
python-multipart


AWS Setup (Explain in Interview)
Create S3 bucket → my-file-upload-bucket
Create DynamoDB table:
Table name: file_metadata
Primary key: file_id (String)
Configure credentials:
aws configure
                  
