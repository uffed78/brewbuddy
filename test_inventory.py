from app.brewfather import import_inventory

def test_import_inventory():
    try:
        inventory = import_inventory()
        print("Inventory importerat:", inventory)
    except Exception as e:
        print("Fel vid import av inventory:", e)

if __name__ == "__main__":
    test_import_inventory()
