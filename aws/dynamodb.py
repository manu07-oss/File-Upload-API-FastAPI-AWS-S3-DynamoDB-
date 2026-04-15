import boto3
from botocore.exceptions import ClientError
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("file_metadata")

def save_metadata(file_id, filename, file_url, size):
    """
    Save file metadata in DynamoDB
    """
    try:
        table.put_item(
            Item={
                "file_id": file_id,
                "filename": filename,
                "file_url": file_url,
                "size": size,
                "uploaded_at": datetime.utcnow().isoformat()
            }
        )
    except ClientError as e:
        print(f"DynamoDB Error: {e}")
        raise Exception("Failed to save metadata")
