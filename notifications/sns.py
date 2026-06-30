import boto3
import os
from dotenv import load_dotenv

load_dotenv()

sns = boto3.client("sns")

TOPIC = os.getenv("SNS_TOPIC_ARN")


def send_sns(subject, message):

    sns.publish(

        TopicArn=TOPIC,

        Subject=subject,

        Message=message
    )
