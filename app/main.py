from app.functions_for_battle.apply_armour import apply_armour
from app.functions_for_battle.apply_potion import apply_potion


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

    # lancelot
    lancelot = knights_config["lancelot"]

    # apply armour
    apply_armour(lancelot)

    # apply weapon
    lancelot["power"] += lancelot["weapon"]["power"]

    # apply potion if exist
    apply_potion(lancelot)

    # arthur
    arthur = knights_config["arthur"]

    # apply armour
    apply_armour(arthur)

    # apply weapon
    arthur["power"] += arthur["weapon"]["power"]

    # apply potion if exist
    apply_potion(arthur)

    # mordred
    mordred = knights_config["mordred"]

    # apply armour
    apply_armour(mordred)

    # apply weapon
    mordred["power"] += mordred["weapon"]["power"]

    # apply potion if exist
    apply_potion(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]

    # apply armour
    apply_armour(red_knight)

    # apply weapon
    red_knight["power"] += red_knight["weapon"]["power"]

    # apply potion if exist
    apply_potion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
