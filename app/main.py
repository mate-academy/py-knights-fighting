from __future__ import annotations
from typing import Any

from app.knights.knight import Knight
from app.actions.fight import knight_fight


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


def create_knight(knight_config: dict[str, Any]) -> dict[str, Knight]:
    return {knight_name: Knight(knight_stats["name"],
                                knight_stats["power"],
                                knight_stats["hp"],
                                knight_stats["armour"],
                                knight_stats["weapon"],
                                knight_stats["potion"])
            for knight_name, knight_stats in knight_config.items()}


def battle(knight_config: dict[str, Any]) -> dict[str, int]:
    ready_knights = create_knight(knight_config)
    print(ready_knights["lancelot"].hp)
    print(ready_knights["lancelot"].power)
    print(ready_knights["lancelot"].protection)
    knight_fight(ready_knights["lancelot"], ready_knights["mordred"])
    print(ready_knights["lancelot"].hp)
    print(ready_knights["lancelot"].power)
    print(ready_knights["lancelot"].protection)
    knight_fight(ready_knights["arthur"], ready_knights["red_knight"])
    return {
        "Lancelot": ready_knights["lancelot"].hp,
        "Artur": ready_knights["arthur"].hp,
        "Mordred": ready_knights["mordred"].hp,
        "Red Knight": ready_knights["red_knight"].hp
    }
