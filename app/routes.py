from flask import Blueprint, jsonify, request
from .utils.brewfather import fetch_inventory, fetch_recipes, fetch_specific_inventory
from .utils.bjcp import fetch_bjcp_styles
from .utils.openai_integration import generate_recipe

main = Blueprint('main', __name__)

@main.route('/brewfather/inventory')
def get_inventory():
    return jsonify(fetch_inventory())

@main.route('/brewfather/inventory/fermentables')
def get_fermentables():
    return jsonify(fetch_specific_inventory("fermentables"))

@main.route('/brewfather/inventory/hops')
def get_hops():
    return jsonify(fetch_specific_inventory("hops"))

@main.route('/brewfather/inventory/yeasts')
def get_yeasts():
    return jsonify(fetch_specific_inventory("yeasts"))

@main.route('/brewfather/recipes')
def get_recipes():
    return jsonify(fetch_recipes())

@main.route('/bjcp-styles')
def get_bjcp_styles():
    return jsonify(fetch_bjcp_styles())

@main.route('/generate-recipe', methods=['POST'])
def generate_recipe_endpoint():
    data = request.json
    context = data.get("context")
    user_input = data.get("user_input")
    recipe = generate_recipe(context, user_input)
    return jsonify({"recipe": recipe})
