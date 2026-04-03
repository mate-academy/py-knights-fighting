from typing import Any

from app.knight.knight_class import Knight


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


def battle(knights: Any) -> dict:

    # KNIGHT PRESENTATION:

    # lancelot
    lancelot = knights["lancelot"]
    lancelot_knight = Knight(lancelot)

    # arthur
    arthur = knights["arthur"]
    arthur_knight = Knight(arthur)

    # mordred
    mordred = knights["mordred"]
    mordred_knight = Knight(mordred)

    # red_knight
    red = knights["red_knight"]
    red_knight = Knight(red)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot_knight.battle(mordred_knight)

    # 2 Arthur vs Red Knight:
    arthur_knight.battle(red_knight)

    # Return battle results:
    return {
        lancelot_knight.name: lancelot_knight.hp,
        arthur_knight.name: arthur_knight.hp,
        mordred_knight.name: mordred_knight.hp,
        red_knight.name: red_knight.hp,
    }


result = battle(KNIGHTS)
print("\nBattle Results:\n")
print(result)
