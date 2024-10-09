import os
from dotenv import load_dotenv
import requests
import datetime
from pprint import pprint
import pandas as pd
import json


load_dotenv()

GH_TOKEN = os.environ["GITHUB_TOKEN"]
GH_USERNAME = os.environ["GITHUB_USERNAME"]


def get_events():
    headers = {
        "accept": "application/vnd.github+json",
        "authorization": f"Bearer {GH_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    api_url = "https://api.github.com/"

    user_events = f"{api_url}users/{GH_USERNAME}/events"

    response = requests.get(url=user_events, headers=headers)
    response.raise_for_status()
    events = response.json()

    return events

# with open("events_req.json", "a") as file:
#     json.dump(events, file)

def format_data():
    events = get_events()

    for event in events:
        event_id = event.id
        event_type = events.type




