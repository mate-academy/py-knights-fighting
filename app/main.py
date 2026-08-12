from app.battle_core.battle import vs_battle, battle_result
from app.battle_core.player import prepare_knight
from typing import Dict

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


def battle(knights_config: Dict) -> Dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = prepare_knight(knights_config["lancelot"])

    # arthur
    arthur = prepare_knight(knights_config["arthur"])

    # mordred
    mordred = prepare_knight(knights_config["mordred"])

    # red_knight
    red_knight = prepare_knight(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot, mordred = vs_battle(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    arthur, red_knight = vs_battle(arthur, red_knight)

    # Return battle results:
    return battle_result(lancelot, mordred, arthur, red_knight)


print(battle(KNIGHTS))
