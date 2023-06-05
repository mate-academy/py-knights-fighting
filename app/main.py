from app.knight import Knight

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


def create_knight(knights_config: dict) -> dict:
    knights = {}
    for name, character in knights_config.items():
        knights[name] = Knight(name=character["name"],
                               power=character["power"],
                               hp=character["hp"],
                               armour=character["armour"],
                               weapon=character["weapon"],
                               potion=character["potion"])

    return knights


def battle(knights_config: dict) -> dict:
    knights = create_knight(knights_config)
    # -------------------------------------------------------------------------------
    # BATTLE:
    battle_schedule = [[knights["lancelot"], knights["mordred"]],
                       [knights["arthur"], knights["red_knight"]]]

    for pair in battle_schedule:
        for i in range(len(pair)):
            pair[i].attack(pair[len(pair) - i - 1])
            pair[i].battle_result()

    # Return battle results:
    res = [knights[name] for name in knights]
    return {knight.name: knight.hp for knight in res}
