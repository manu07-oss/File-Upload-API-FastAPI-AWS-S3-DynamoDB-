import boto3
from botocore.exceptions import ClientError

# Create S3 client
s3_client = boto3.client("s3")

BUCKET_NAME = "my-file-upload-bucket"

def upload_file_to_s3(file_obj, filename):
    """
    Uploads file to S3 bucket

    Args:
        file_obj: file object
        filename: name of file

    Returns:
        file_url (str)
    """
    try:
        s3_client.upload_fileobj(file_obj, BUCKET_NAME, filename)

        # Construct file URL
        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
        return file_url

    except ClientError as e:
        print(f"S3 Upload Error: {e}")
        raise Exception("Failed to upload file to S3")
