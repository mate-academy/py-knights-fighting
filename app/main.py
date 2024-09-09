from app.knights.class_knight import Knight
from typing import Dict, Any

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


def create_knights(knights_data: Dict[str, Any]) -> dict:
    knights = {}
    for key, data in knights_data.items():
        knights[key] = Knight(**data)
    return knights


def battle(all_knight: KNIGHTS) -> dict:
    knights = create_knights(all_knight)
    for knight in knights.values():
        knight.prepare_for_battle()
    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.total_hp -= mordred.total_power
    mordred.total_hp -= lancelot.total_power

    # check if someone fell in battle
    if lancelot.total_hp <= 0:
        lancelot.total_hp = 0

    if mordred.total_hp <= 0:
        mordred.total_hp = 0

    # 2 Arthur vs Red Knight:
    arthur.total_hp -= red_knight.total_power
    red_knight.total_hp -= arthur.total_power

    # check if someone fell in battle
    if arthur.total_hp <= 0:
        arthur.total_hp = 0

    if red_knight.total_hp <= 0:
        red_knight.total_hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.total_hp,
        arthur.name: arthur.total_hp,
        mordred.name: mordred.total_hp,
        red_knight.name: red_knight.total_hp,
    }


print(battle(KNIGHTS))
