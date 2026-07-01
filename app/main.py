from app.apply_knight_characteristic.prepare_knights import prepare_knight
from app.battle.check_fell import check_fell
from app.battle.knight_vs_knight import knight_vs_knight
from app.battle.result import result

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

    names = ["lancelot", "arthur", "mordred", "red_knight"]

    knights_list = [lancelot, arthur, mordred, red_knight] = \
        [knights_config[name] for name in names]
    # lancelot = knights_config["lancelot"]
    # arthur = knights_config["arthur"]
    # mordred = knights_config["mordred"]
    # red_knight = knights_config["red_knight"]
    prepare_knight(knights_list)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knight_vs_knight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    knight_vs_knight(arthur, red_knight)

    # check if someone fell in battle

    for knight in [arthur, red_knight, lancelot, mordred]:
        check_fell(knight)

    # Return battle results:
    return result([lancelot, arthur, mordred, red_knight])
