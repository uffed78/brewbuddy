from flask import Flask, jsonify, request
from app.utils.beer_styles import load_beer_styles, search_beer_styles, filter_beer_styles_by_ingredients
import os
from flask import Flask, jsonify
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
from flask import render_template
from app.routes import main



# Ladda miljövariabler från .env-filen
load_dotenv()

# Hämta API-nyckel och användarnamn från .env
USERNAME = os.getenv("BREWFATHER_USERNAME")
API_KEY = os.getenv("BREWFATHER_API_KEY")

# Flask-app
app = Flask(__name__, static_folder='app/static', template_folder='app/templates')
app.register_blueprint(main, url_prefix='/api')

# Ladda ölstilsdatabasen
beer_styles = load_beer_styles()

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

@app.route('/api/styles', methods=['GET'])
def get_beer_styles():
    """
    Hämta alla ölstilar.
    """
    return jsonify(beer_styles), 200

@app.route('/api/styles/search', methods=['GET'])
def search_styles():
    """
    Sök efter ölstilar baserat på en term (namn eller kategori).
    """
    search_term = request.args.get('term', '')
    if not search_term:
        return jsonify({"error": "Ingen sökterm angiven"}), 400

    results = search_beer_styles(beer_styles, search_term)
    return jsonify(results), 200

@app.route('/api/styles/filter', methods=['POST'])
def filter_styles():
    """
    Filtrera ölstilar baserat på tillgängliga ingredienser.
    """
    data = request.get_json()
    available_ingredients = set(data.get('ingredients', []))

    if not available_ingredients:
        return jsonify({"error": "Inga ingredienser angivna"}), 400

    matching_styles = filter_beer_styles_by_ingredients(beer_styles, available_ingredients)
    return jsonify(matching_styles), 200

@app.route('/')
def index():
    return render_template('index.html')


# Starta Flask-applikationen
if __name__ == '__main__':
    app.run(debug=True)
