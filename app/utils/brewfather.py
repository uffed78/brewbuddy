import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("BREWFATHER_USERNAME")
API_KEY = os.getenv("BREWFATHER_API_KEY")

def fetch_inventory():
    url = "https://api.brewfather.app/v2/inventory"
    auth = HTTPBasicAuth(USERNAME, API_KEY)
    response = requests.get(url, auth=auth)
    return response.json() if response.status_code == 200 else {"error": response.text}

def fetch_specific_inventory(resource_type):
    url = f"https://api.brewfather.app/v2/inventory/{resource_type}"
    auth = HTTPBasicAuth(USERNAME, API_KEY)
    response = requests.get(url, auth=auth)
    return response.json() if response.status_code == 200 else {"error": response.text}

def fetch_recipes():
    url = "https://api.brewfather.app/v2/recipes"
    auth = HTTPBasicAuth(USERNAME, API_KEY)
    response = requests.get(url, auth=auth)
    return response.json() if response.status_code == 200 else {"error": response.text}
