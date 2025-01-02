import os
from dotenv import load_dotenv

# Ladda miljövariabler från .env
load_dotenv()

# Hämta värdena
api_key = os.getenv('BREWFATHER_API_KEY')
username = os.getenv('BREWFATHER_USERNAME')

# Skriv ut värdena
print(f"Loaded API Key: {api_key}")
print(f"Loaded Username: {username}")
