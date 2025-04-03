# app/main.py
from app.knight import Knight
from app.battle import battle

# Define knights_dict as your knight data
knights_dict = {
    "Lancelot": {
        "name": "Lancelot",
        "power": 100,
        "hp": 100,
        "armour": [{'part': 'helmet', 'protection': 20}],
        "weapon": {"name": "Sword", "power": 50},
        "potion": {"name": "Blessing", "effect": {"hp": 20, "power": 10}}
    },
    "Arthur": {
        "name": "Arthur",
        "power": 80,
        "hp": 120,
        "armour": [{'part': 'helmet', 'protection': 25}],
        "weapon": {"name": "Sword", "power": 60},
        "potion": None
    },
    "Mordred": {
        "name": "Mordred",
        "power": 90,
        "hp": 100,
        "armour": [{'part': 'helmet', 'protection': 15}, {'part': 'breastplate', 'protection': 20}],
        "weapon": {"name": "Axe", "power": 70},
        "potion": None
    },
    "Red Knight": {
        "name": "Red Knight",
        "power": 80,
        "hp": 70,
        "armour": [{'part': 'helmet', 'protection': 10}],
        "weapon": {"name": "Spear", "power": 40},
        "potion": {"name": "Potion of Might", "effect": {"hp": 10, "power": 20}},
    },
}

# Convert knights_dict into a list of Knight objects
knights_list = [Knight(**knight_data) for knight_data in knights_dict.values()]


def main():
    # Now you can pass knights_list to the battle function
    results = battle(knights_dict)  # Use knights_list here

    # Display results
    for knight in results:
        print(f"{knight} has {results[knight]} HP remaining.")


if __name__ == "__main__":
    main()
