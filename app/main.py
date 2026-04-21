from typing import Dict, List
from app.Knights.knights import Knights, battle as fight_logic


KNIGHTS: Dict[str, Dict[str, any]] = {
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

lancelot: Knights = Knights(KNIGHTS["lancelot"])
arthur: Knights = Knights(KNIGHTS["arthur"])
mordred: Knights = Knights(KNIGHTS["mordred"])
red_knight: Knights = Knights(KNIGHTS["red_knight"])

all_knights: List[Knights] = [lancelot, arthur, mordred, red_knight]
for knight in all_knights:
    knight.prepare_for_battle()


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knights(data)
        for name, data in knights_config.items()
    }
    for knight in knights.values():
        knight.prepare_for_battle()
    fight_logic(knights["lancelot"], knights["mordred"])
    fight_logic(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


results: Dict[str, int] = {knight.name: knight.hp for knight in all_knights}

print(results)
