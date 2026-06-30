import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ses = boto3.client("ses")

FROM = os.getenv("EMAIL_FROM")

TO = os.getenv("EMAIL_TO")


def send_email(subject, body):

    ses.send_email(

        Source=FROM,

        Destination={"ToAddresses": [TO]},

        Message={

            "Subject": {"Data": subject},

            "Body": {

                "Text": {

                    "Data": body

                }

            }

        }

    )
