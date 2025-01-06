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

def filter_ingredients(inventory):
    """
    Låter användaren exkludera ingredienser från en inventeringslista.
    :param inventory: Lista med ingredienser.
    :return: Filtrerad lista med ingredienser.
    """
    if not inventory:
        print("Inventariet är tomt eller saknas.")
        return []

    print("\nTillgängliga ingredienser:")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']}")  # Anta att varje ingrediens har ett 'name'-fält

    print("\nSkriv numren för ingredienserna du vill exkludera, separerade med kommatecken (t.ex. 1,3,5):")
    exclude_indices = input("Dina val: ").strip()
    exclude_indices = [int(i) - 1 for i in exclude_indices.split(",") if i.isdigit()]

    filtered_inventory = [
        item for i, item in enumerate(inventory) if i not in exclude_indices
    ]

    print("\nEfter filtrering:")
    for item in filtered_inventory:
        print(f"- {item['name']}")

    return filtered_inventory
