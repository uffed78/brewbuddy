import requests
import os
from dotenv import load_dotenv

# Ladda miljövariabler från .env
load_dotenv()

def fetch_inventory():
    """
    Hämtar inventory från Brewfather API med användarnamn och API-nyckel.
    """
    api_key = os.getenv('BREWFATHER_API_KEY')
    username = os.getenv('BREWFATHER_USERNAME')

    if not api_key or not username:
        return {"error": "Brewfather API Key eller användarnamn saknas"}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    base_url = f"https://api.brewfather.app/v2/inventory"

    try:
        fermentables_response = requests.get(f"{base_url}/fermentables", headers=headers)
        hops_response = requests.get(f"{base_url}/hops", headers=headers)
        yeast_response = requests.get(f"{base_url}/yeast", headers=headers)

        # Debug-utskrift för att se API-svar
        print(f"Fermentables response: {fermentables_response.status_code}, {fermentables_response.text}")

        if fermentables_response.status_code != 200:
            return {"error": f"Fel vid hämtning av fermentables: {fermentables_response.text}"}
        
        return {
            "fermentables": fermentables_response.json(),
            "hops": hops_response.json(),
            "yeast": yeast_response.json()
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Fel vid API-anrop: {str(e)}"}

def fetch_recipes():
    """
    Hämtar recept från Brewfather API.
    """
    api_key = os.getenv('BREWFATHER_API_KEY')
    username = os.getenv('BREWFATHER_USERNAME')

    if not api_key or not username:
        return {"error": "Brewfather API Key eller användarnamn saknas"}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    url = f"https://api.brewfather.app/v2/recipes"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return {"error": f"Fel vid hämtning av recept: {response.text}"}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Fel vid API-anrop: {str(e)}"}
