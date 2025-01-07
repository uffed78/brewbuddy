from openai import OpenAI

# Initialisera OpenAI-klienten
client = OpenAI()



def generate_recipe(bjcp_style, inventory):
    """
    Genererar ett recept baserat på BJCP-stil och tillgängligt inventory.

    Args:
        bjcp_style (dict): En BJCP-stil, t.ex. {"name": "Pale Ale", "description": "..."}
        inventory (dict): Användarens tillgängliga ingredienser.

    Returns:
        str: Ett recept genererat av OpenAI.
    """
    try:
        # Skapa meddelandekontext för GPT
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

        # Anropa GPT med den korrekta metoden
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        # Returnera GPT:s svar
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Exception: {str(e)}")
        return f"Error generating recipe: {str(e)}"


from openai import OpenAI
client = OpenAI()

def suggest_beer_styles(ingredients):
    """
    Använd ChatGPT för att föreslå ölstilar baserat på användarens ingredienser.
    """
    prompt = f"Jag har följande ingredienser: {', '.join(ingredients)}. Vilka ölstilar kan jag brygga med dessa ingredienser?"

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer", "content": "You are a helpful assistant that specializes in brewing beer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Fel vid anrop till OpenAI: {str(e)}"

def generate_recipe_with_gpt(beer_style, ingredients):
    """
    Använd ChatGPT för att generera ett ölrecept baserat på stil och ingredienser.
    """
    prompt = (
        f"Jag vill brygga en {beer_style}. "
        f"Jag har följande ingredienser: {', '.join(ingredients)}. "
        "Skapa ett komplett ölrecept med stegvisa instruktioner, ingrediensmängder och jästemperatur."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer", "content": "Du är en AI-expert på att skapa ölrecept."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Fel vid anrop till OpenAI: {str(e)}"
