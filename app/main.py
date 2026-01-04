from app.knigts import Knight

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
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
        "potion": None,
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


def battle(knights_config: dict) -> dict:
    # Preparations
    dict_of_knights = {}
    for knight_name, value in knights_config.items():
        knight = Knight(
            value.get("name"),
            value.get("power"),
            value.get("hp")
        )
        knight.apply_armour(value.get("armour"))
        knight.apply_weapon(value.get("weapon"))
        knight.apply_potion(value.get("potion"))
        dict_of_knights[value.get("name")] = knight

    # Battle
    Knight.battle(
        dict_of_knights.get("Lancelot"),
        dict_of_knights.get("Mordred")
    )
    Knight.battle(
        dict_of_knights.get("Artur"),
        dict_of_knights.get("Red Knight")
    )

    return {
        dict_of_knights.get(knight).name: dict_of_knights.get(knight).hp
        for knight in dict_of_knights
    }
