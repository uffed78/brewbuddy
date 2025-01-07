from openai import OpenAI

# Initialisera OpenAI-klienten
client = OpenAI()

def generate_recipe(bjcp_style, inventory):
    """Generera ett ölrecept baserat på BJCP-stil och inventory."""
    try:
        messages = [
            {"role": "developer", "content": "You are a helpful assistant that generates beer recipes."},
            {"role": "user", "content": (
                f"Create a beer recipe based on the following BJCP style:\n"
                f"Name: {bjcp_style['name']}\n"
                f"Description: {bjcp_style['description']}\n\n"
                f"Use the following ingredients from the inventory:\n"
                f"Malts: {', '.join([m['name'] for m in inventory['fermentables']])}\n"
                f"Hops: {', '.join([h['name'] for h in inventory['hops']])}\n"
                f"Yeasts: {', '.join([y['name'] for y in inventory['yeasts']])}\n\n"
                f"Generate a detailed recipe including ingredient amounts, brewing steps, and fermentation times."
            )}
        ]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating recipe: {str(e)}"

def handle_chat(user_input):
    """Hantera användarens meddelande i chatten."""
    try:
        messages = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error handling chat: {str(e)}"
