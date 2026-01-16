from app.knights.knight import Knight
from app.battle.battle import Battle

"""
This main.py module contains the "battle" function
and KNIGHT config. Function takes KNIGHT config to
get the data, creates instances of particular knights,
performs "battle" calculations and returns final result.
"""


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


def battle(config):
    """
    Function creates two battles, with four
    knights, and returns one sliced result of
    both battles. It can be changed to return
    result of one battle apart from other. For
    large quantity of knights and battles it should
    perform 'for' loops, but now it`s not implemented.
    """
    lancelot = Knight("lancelot", config)
    arthur = Knight("arthur", config)
    mordred = Knight("mordred", config)
    red_knight = Knight("red_knight", config)

    result = Battle.get_result(lancelot, mordred)
    result2 = Battle.get_result(arthur, red_knight)
    result.update(result2)

    return result
