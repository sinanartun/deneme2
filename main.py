import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get AWS credentials from environment variables
access_key = os.getenv('access_key')
secret_key = os.getenv('secret_key')

# Initialize a session using Amazon S3
s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

# List S3 buckets
response = s3.list_buckets()

# Print bucket names
print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
