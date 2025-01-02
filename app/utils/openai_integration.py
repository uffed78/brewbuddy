from openai import OpenAI
import os
from dotenv import load_dotenv

# Ladda miljövariabler från .env-filen
load_dotenv()

# Skapa en klientinstans för OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_recipe(user_input):
    """
    Generera ett ölrecept baserat på användarens input.
    """
    prompt = f"""
    Du är en erfaren ölbryggare som guidar användare genom att skapa ölrecept.
    Användarens input:
    - Ölstil: {user_input['style']}
    - Alkoholstyrka: {user_input['alcohol']}%
    - Smakprofil: {user_input['flavor']}
    Skapa ett recept baserat på dessa specifikationer:
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Ange rätt modell beroende på din konfiguration
            messages=[
                {"role": "system", "content": "Du är en professionell bryggmästare och expert på ölbryggning."},
                {"role": "user", "content": prompt}
            ]
        )
        # Returnera meddelandets innehåll direkt
        return completion.choices[0].message.content
    except Exception as e:
        # Hantera fel och returnera ett läsbart meddelande
        return f"Ett fel uppstod vid generering av receptet: {str(e)}"
