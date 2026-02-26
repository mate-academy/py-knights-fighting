from app.knight import Knight
from app.battle import perform_battle

knights_config = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": {
            "name": "Magic Power",
            "effect": {
                "power": +25,
                "hp": +10,
            }
        }
    },
    "arthur": {
        "name": "Arthur",
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
        "potion": {
            "name": "Dragon's heart",
            "effect": {
                "protection": +20,
                "power": +10,
                "hp": +10,
            }
        }
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle(knights: dict) -> dict:
    knight_dict = {
        key: Knight(value) for (key, value) in knights.items()}
    first_battle = perform_battle(knight_dict["lancelot"],
                                  knight_dict["mordred"])
    second_battle = perform_battle(knight_dict["arthur"],
                                   knight_dict["red_knight"])

    return {"Lancelot": first_battle["Lancelot"],
            "Arthur": second_battle["Arthur"],
            "Mordred": first_battle["Mordred"],
            "Red Knight": second_battle["Red Knight"]}
