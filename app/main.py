from app.knights.knight import Knight


# creation of knights


def knights_config(knights_data: dict) -> dict:
    knights_dict = {}
    for knight_name, knight_data in knights_data.items():
        knight = Knight(
            knight_data["name"],
            knight_data["power"],
            knight_data["hp"],
        )
        knight.protection = 0
        knight.apply_armour(knight_data["armour"])
        knight.apply_weapon(knight_data["weapon"])
        knight.apply_potion(knight_data["potion"])
        knights_dict[knight_name] = knight
    return knights_dict


# BATTLE
def battle(knights_dict: dict[str, Knight]) -> dict[str, int]:

    knight1 = knights_dict["lancelot"]
    knight2 = knights_dict["mordred"]

    knight1.attack(knight2)
    knight2.attack(knight1)
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}



knights_data = {
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

knights_dict = knights_config(knights_data)


battle_result = battle(knights_dict)
print(battle_result)

