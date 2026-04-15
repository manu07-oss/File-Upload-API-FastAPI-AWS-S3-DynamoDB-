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


▶️ Run the Application
uvicorn app:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs
🧪 Example Test

Upload:

File: resume.pdf

Response:

{
  "file_id": "123e4567",
  "filename": "resume.pdf",
  "file_url": "https://my-file-upload-bucket.s3.amazonaws.com/resume.pdf",
  "size": 24567
}
💡 Interview Explanation (VERY IMPORTANT)
🔹 How to explain flow:

“When a client uploads a file, my FastAPI service receives it, generates a unique ID, and uploads the file to S3 using boto3. After successful upload, I store metadata like filename, size, and timestamp in DynamoDB. I’ve added error handling to ensure failures in S3 or DB are properly captured.”

🔹 Error Handling Strategy
S3 failure → throw exception
DynamoDB failure → rollback logic (can mention improvement)
API failure → HTTP 500 response
🔹 Improvements (Say This in Interview ⭐)
Add pre-signed URLs instead of direct upload
Add file validation (type/size)
Use IAM roles instead of hardcoded credentials
Add logging (CloudWatch)
Add retry mechanism (boto3 config)
Add async processing (SQS + Lambda)
🔹 DevOps Angle (Bonus Points 💥)

Since you're a DevOps Engineer, say:

“I can containerize this using Docker”
“Deploy on ECS/EKS”
“Use Terraform for infra (S3 + DynamoDB)”
“Add CI/CD via GitLab pipeline”
                  
