from __future__ import annotations
from typing import Any

from app.knights.knight import Knight


# creation of knights


def knights_config(knights: dict[str, Any]) -> dict:
    return {knight_name: Knight(
            knight_data["name"],
            knight_data["power"],
            knight_data["hp"],
            knight_data["armour"],
            knight_data["weapon"],
            knight_data["potion"]) for
            knight_name, knight_data in knights.items()}


# BATTLE
def battle(knights: dict[str, Any]) -> dict[str, int]:
    ready_knights = knights_config(knights)
    for attacker, defender in [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]:
        attacker_knight = ready_knights[attacker]
        defender_knight = ready_knights[defender]

        Knight.attack(attacker_knight, defender_knight)

        attacker_knight.check_hp()
        defender_knight.check_hp()

    return {
        knight.name: knight.hp for knight in ready_knights.values()
    }


knights = {
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
