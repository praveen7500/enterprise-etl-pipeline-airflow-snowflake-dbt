import boto3
from logger import logger
from dotenv import load_dotenv
import os

load_dotenv()

def upload(file_name):

    bucket = os.getenv("S3_BUCKET")

    s3 = boto3.client("s3")

    s3.upload_file(file_name, bucket, file_name)

    logger.info("Uploaded to S3")
