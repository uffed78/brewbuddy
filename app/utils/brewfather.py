import requests

def fetch_inventory(api_key, username):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    base_url = f"https://api.brewfather.app/v2/inventory"

    inventory = {
        "fermentables": requests.get(f"{base_url}/fermentables", headers=headers).json(),
        "hops": requests.get(f"{base_url}/hops", headers=headers).json(),
        "yeast": requests.get(f"{base_url}/yeast", headers=headers).json(),
    }
    return inventory
