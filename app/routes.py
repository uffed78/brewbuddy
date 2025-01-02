import os
from flask import Blueprint, render_template, request, jsonify
from app.utils.openai_integration import generate_recipe
from app.utils.brewfather import fetch_inventory

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/create-recipe', methods=['POST'])
def create_recipe():
    user_input = request.json
    recipe = generate_recipe(user_input)
    return jsonify(recipe)

@main.route('/brewfather-inventory', methods=['GET'])
def brewfather_inventory():
    api_key = request.args.get('api_key')
    username = request.args.get('username')
    inventory = fetch_inventory(api_key, username)
    return jsonify(inventory)
