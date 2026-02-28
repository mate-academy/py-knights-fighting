from typing import Any

from app.knight import Knight   # app.knight instead of knight for pytest
from app.tournament import Lists


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


def preparation(knights_config: dict[str, dict[str, Any]]) -> None:
    Knight.knights_enlisted.clear()

    for knight in knights_config.values():
        Lists.enlist_knight(knight)
        Lists.take_knight_to_armoury(knight)


def battle(knights_config: dict[str, dict[str, Any]]) -> dict[str, int]:
    preparation(knights_config)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # fights: Lancelot vs Mordred, Arthur vs Red Knight
    pairs = [("Lancelot", "Mordred"), ("Arthur", "Red Knight")]

    for pair in pairs:
        Knight.knights_enlisted[pair[0]].fight(
            Knight.knights_enlisted[pair[1]]
        )

    # Return battle results:
    return {
        knight.name: knight.health
        for knight in Knight.knights_enlisted.values()
    }


print(battle(KNIGHTS))
