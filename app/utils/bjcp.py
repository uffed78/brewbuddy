import os
import json

def fetch_bjcp_styles():
    """
    Läser BJCP-stilar från en lokal JSON-fil.
    """
    file_path = os.path.join(os.path.dirname(__file__), "bjcp_styles.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": f"Fel vid läsning av BJCP-stilar: {str(e)}"}
