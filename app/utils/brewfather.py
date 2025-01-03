import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Ladda miljövariabler från .env
load_dotenv()

# Konstanter för API-nyckel och användarnamn
API_KEY = os.getenv('BREWFATHER_API_KEY')
USERNAME = os.getenv('BREWFATHER_USERNAME')

def validate_credentials():
    """
    Validerar att API-nyckeln och användarnamnet finns.
    """
    if not API_KEY or not USERNAME:
        return {"error": "Brewfather API Key eller användarnamn saknas"}
    return None

def fetch_inventory():
    """
    Hämtar hela inventariet från Brewfather API.
    """
    validation_error = validate_credentials()
    if validation_error:
        return validation_error

    base_url = "https://api.brewfather.app/v2/inventory"
    auth = HTTPBasicAuth(USERNAME, API_KEY)

    try:
        response = requests.get(base_url, auth=auth)
        if response.status_code != 200:
            return {"error": f"Fel vid hämtning av inventariet: {response.text}"}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Fel vid API-anrop: {str(e)}"}

def fetch_specific_inventory(resource_type):
    """
    Hämtar specifik typ av inventarier (fermentables, hops, yeasts) från Brewfather API.
    """
    validation_error = validate_credentials()
    if validation_error:
        return validation_error

    url = f"https://api.brewfather.app/v2/inventory/{resource_type}"
    auth = HTTPBasicAuth(USERNAME, API_KEY)

    try:
        response = requests.get(url, auth=auth)
        if response.status_code != 200:
            return {"error": f"Fel vid hämtning av {resource_type}: {response.text}"}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Fel vid API-anrop: {str(e)}"}

def fetch_recipes():
    """
    Hämtar recept från Brewfather API.
    """
    validation_error = validate_credentials()
    if validation_error:
        return validation_error

    url = "https://api.brewfather.app/v2/recipes"
    auth = HTTPBasicAuth(USERNAME, API_KEY)

    try:
        response = requests.get(url, auth=auth)
        if response.status_code != 200:
            return {"error": f"Fel vid hämtning av recept: {response.text}"}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Fel vid API-anrop: {str(e)}"}
