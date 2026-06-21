from app.battle.battle import Battle
from app.knights.knight import Knight
from app.knights.potion import Potion
from app.knights.protection import Protection
from app.knights.weapon import Weapon

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


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = []

    for knight in knights_config:
        knights.append(Knight.create_knight(knights_config[knight]))

    for knight in knights:
        Protection.apply_protection(knight)
        Weapon.apply_weapon(knight)
        Potion.apply_potion(knight)

    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # # 1 Lancelot vs Mordred:
    Battle.begin_battle(lancelot, mordred)
    # # 2 Arthur vs Red Knight:
    Battle.begin_battle(arthur, red_knight)

    return Battle.result_of_battle(lancelot, arthur, mordred, red_knight)


print(battle(KNIGHTS))
