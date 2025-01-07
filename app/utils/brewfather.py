import requests
import os
from dotenv import load_dotenv

# Ladda miljövariabler
load_dotenv()

def fetch_inventory():
    """Hämta användarens inventory från Brewfather."""
    api_key = os.getenv('BREWFATHER_API_KEY')
    username = os.getenv('BREWFATHER_USERNAME')

    if not api_key or not username:
        return {"error": "Brewfather API Key eller användarnamn saknas"}

    headers = {"Authorization": f"Bearer {api_key}"}
    base_url = "https://api.brewfather.app/v2/inventory"

    try:
        fermentables = requests.get(f"{base_url}/fermentables", headers=headers).json()
        hops = requests.get(f"{base_url}/hops", headers=headers).json()
        yeasts = requests.get(f"{base_url}/yeasts", headers=headers).json()

        return {"fermentables": fermentables, "hops": hops, "yeasts": yeasts}
    except requests.exceptions.RequestException as e:
        return {"error": f"Fel vid API-anrop: {str(e)}"}

def fetch_recipes():
    """Hämta användarens recept från Brewfather."""
    api_key = os.getenv('BREWFATHER_API_KEY')
    username = os.getenv('BREWFATHER_USERNAME')

    if not api_key or not username:
        return {"error": "Brewfather API Key eller användarnamn saknas"}

    headers = {"Authorization": f"Bearer {api_key}"}
    url = "https://api.brewfather.app/v2/recipes"

    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Fel vid API-anrop: {str(e)}"}
