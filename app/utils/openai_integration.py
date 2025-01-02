from openai import OpenAI
import os
from dotenv import load_dotenv

# Ladda miljövariabler
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_recipe(context, user_input):
    """
    Skapar recept baserat på val (lager, recept, BJCP-stilar).
    """
    if context == "inventory":
        prompt = f"""
        Du är en erfaren ölbryggare. Använd följande lager för att skapa ett recept:
        {user_input}
        Guidar användaren steg för steg till att skapa ett ölrecept.
        """
    elif context == "recipe":
        prompt = f"""
        Du är en erfaren ölbryggare. Följande recept ska utvecklas:
        {user_input}
        Hjälp användaren att justera och förbättra receptet.
        """
    elif context == "bjcp":
        prompt = f"""
        Du är en erfaren ölbryggare. Använd följande BJCP-stil:
        {user_input}
        Guidar användaren steg för steg till att skapa ett ölrecept enligt denna stil.
        """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Du är en professionell bryggmästare."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ett fel uppstod vid generering av receptet: {str(e)}"
