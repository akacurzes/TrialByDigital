import os
import requests

def get_iam_token():
    api_key = os.getenv("IBM_CLOUD_API_KEY")
    response = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data={"apikey": api_key, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json()["access_token"]
