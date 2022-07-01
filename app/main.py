from app.solution.knights_creation import Knights


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


def battle(kn_dict: dict):
    info = Knights.transformation(kn_dict)
    arthur = Knights(info["arthur"][0], info["arthur"][1],
                     info["arthur"][2], info["arthur"][3])
    lancelot = Knights(info["lancelot"][0], info["lancelot"][1],
                       info["lancelot"][2], info["lancelot"][3])
    mordred = Knights(info["mordred"][0], info["mordred"][1],
                      info["mordred"][2], info["mordred"][3])
    red_knight = Knights(info["red_knight"][0], info["red_knight"][1],
                         info["red_knight"][2], info["red_knight"][3])
    arthur.one_battle(red_knight)
    lancelot.one_battle(mordred)
    heroes = [arthur, lancelot, mordred, red_knight]
    return {hero.name: hero.hp for hero in heroes}
