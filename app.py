import os
from flask import Flask, jsonify
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth

# Ladda miljövariabler från .env-filen
load_dotenv()

# Hämta API-nyckel och användarnamn från .env
USERNAME = os.getenv("BREWFATHER_USERNAME")
API_KEY = os.getenv("BREWFATHER_API_KEY")

# Flask-app
app = Flask(__name__)

# Funktion för att hämta data från Brewfather API
def fetch_inventory(resource_type):
    """
    Hämtar specifik inventory-data från Brewfather API med Basic Auth.
    resource_type: 'fermentables', 'hops', eller 'yeasts'
    """
    url = f"https://api.brewfather.app/v2/inventory/{resource_type}"
    auth = HTTPBasicAuth(USERNAME, API_KEY)  # Använd Basic Auth
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Flask-route för att hämta fermentables
@app.route('/api/inventory/fermentables', methods=['GET'])
def get_fermentables():
    data = fetch_inventory("fermentables")
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch fermentables"}), 500

# Flask-route för att hämta hops
@app.route('/api/inventory/hops', methods=['GET'])
def get_hops():
    data = fetch_inventory("hops")
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch hops"}), 500

# Flask-route för att hämta yeasts
@app.route('/api/inventory/yeasts', methods=['GET'])
def get_yeasts():
    data = fetch_inventory("yeasts")
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch yeasts"}), 500

# Starta Flask-applikationen
if __name__ == '__main__':
    app.run(debug=True)
