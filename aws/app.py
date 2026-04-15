from fastapi import FastAPI, UploadFile, File, HTTPException
import uuid

from aws.s3 import upload_file_to_s3
from aws.dynamodb import save_metadata

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload file API

    Steps:
    1. Generate unique file ID
    2. Upload file to S3
    3. Store metadata in DynamoDB
    """

    try:
        # Generate unique file ID
        file_id = str(uuid.uuid4())

        # Read file content
        contents = await file.read()
        file_size = len(contents)

        # Upload to S3
        file_url = upload_file_to_s3(file.file, file.filename)

        # Save metadata to DynamoDB
        save_metadata(file_id, file.filename, file_url, file_size)

        return {
            "file_id": file_id,
            "filename": file.filename,
            "file_url": file_url,
            "size": file_size
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
