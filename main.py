from app.knight.knight import Knight
from app.battle.knights_battle import KnightsBattle
from app.knight.armour import Armour
from app.knight.weapon import Weapon
from app.knight.potion import Potion
from app.helpers.create_knight import create_knight


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


def battle(knightsConfig: dict) -> dict[str, int]:
    # BATTLE PREPARATIONS:
    knights = []
    for knight in knightsConfig:
        kn = create_knight(knightsConfig[knight])
        #Calculate stats
        kn.calculate_stats()
        knights.append(kn)
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    KnightsBattle.knights_battle(knights[0], knights[2])

    # 2 Arthur vs Red Knight:
    KnightsBattle.knights_battle(knights[1], knights[3])

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in knights
    }

print(battle(KNIGHTS))
