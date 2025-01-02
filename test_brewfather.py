import requests
import os
from dotenv import load_dotenv

# Ladda miljövariabler
load_dotenv()

# Hämta nyckel och användarnamn
api_key = os.getenv('BREWFATHER_API_KEY')
username = os.getenv('BREWFATHER_USERNAME')

# Definiera headers och URL
headers = {
    "Authorization": f"Bearer {api_key}",  # Korrigerat till "Bearer"
    "Content-Type": "application/json"
}
url = "https://api.brewfather.app/v2/inventory/fermentables"

# Gör API-anropet
response = requests.get(url, headers=headers)

# Skriv ut resultat
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
