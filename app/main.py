from app.calculation_stats.apply_armour import ApplyArmour
from app.calculation_stats.apply_potion import ApplyPotion
from app.calculation_stats.apply_weapon import ApplyWeapon
from app.battle_knights.check_death import CheckDeath
from app.battle_knights.mortal_combat import Combat


Knights = {
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
        "name": "Artur",
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
    ApplyArmour(lancelot)

    # apply weapon
    ApplyWeapon(lancelot)

    # apply potion if exist
    ApplyPotion(lancelot)

    # arthur
    arthur = knights_config["arthur"]

    # apply armour
    ApplyArmour(arthur)

    # apply weapon
    ApplyWeapon(arthur)

    # apply potion if exist
    ApplyPotion(arthur)

    # mordred
    mordred = knights_config["mordred"]

    # apply armour
    ApplyArmour(mordred)

    # apply weapon
    ApplyWeapon(mordred)

    # apply potion if exist
    ApplyPotion(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]

    # apply armour
    ApplyArmour(red_knight)

    # apply weapon
    ApplyWeapon(red_knight)

    # apply potion if exist
    ApplyPotion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Combat(lancelot, mordred)

    # check if someone fell in battle
    CheckDeath(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    Combat(arthur, red_knight)

    # check if someone fell in battle
    CheckDeath(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(Knights))
