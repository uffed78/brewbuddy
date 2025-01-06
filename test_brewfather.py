import sys
import os

# Lägg till sökvägen till app/utils i sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app', 'utils'))

from brewfather import fetch_specific_inventory, filter_ingredients

def test_fetch_and_filter_inventory(resource_type):
    try:
        inventory = fetch_specific_inventory(resource_type)
        if "error" in inventory:
            print(f"Fel vid hämtning av inventory för {resource_type}:", inventory["error"])
            return

        print(f"Inventory för {resource_type} importerat.")
        filtered_inventory = filter_ingredients(inventory)
        print("\nFiltrerad inventering:")
        print(filtered_inventory)
    except Exception as e:
        print("Ett oväntat fel inträffade:", e)

if __name__ == "__main__":
    resource_type = input("Ange vilken typ av inventory du vill hämta (fermentables, hops, yeasts): ").strip()
    test_fetch_and_filter_inventory(resource_type)
