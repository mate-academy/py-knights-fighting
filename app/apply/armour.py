def apply_armour(knight):
    knight["protection"] = 0
    for part in knight["armour"]:
        knight["protection"] += part["protection"]
    return knight["protection"]


if __name__ == '__main__':
    arthur = {
        "name": "Artur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    }
    print(apply_armour(arthur))

