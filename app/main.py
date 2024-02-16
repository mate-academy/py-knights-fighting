from app.preparations.armour import apply_armour
from app.preparations.weapon import apply_weapon
from app.preparations.potion import apply_potion_if_exist
from app.battle.check_fell import check_fell
from app.battle.battle_results import results_hp


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


def battle(knights_config: dict) -> None:
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = knights_config["lancelot"]
    # arthur
    arthur = knights_config["arthur"]
    # mordred
    mordred = knights_config["mordred"]
    # red_knight
    red_knight = knights_config["red_knight"]

    for knight_name, knight_data in knights_config.items():
        # BATTLE PREPARATIONS:
        apply_armour(knight_data)
        apply_weapon(knight_data)
        apply_potion_if_exist(knight_data)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    results_hp(lancelot, mordred)

    # check if someone fell in battle
    check_fell(lancelot)
    check_fell(mordred)

    # 2 Arthur vs Red Knight:
    results_hp(arthur, red_knight)

    # check if someone fell in battle
    check_fell(arthur)
    check_fell(red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
