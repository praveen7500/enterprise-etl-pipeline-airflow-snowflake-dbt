import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("SLACK_WEBHOOK")


def send_slack(message):

    payload = {

        "text": message

    }

    requests.post(WEBHOOK, json=payload)
