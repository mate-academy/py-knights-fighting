from app.knights.characteristics import KnightsCharacteristics
from app.battle.battle_logic import Battle

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

    lancelot_stats = KnightsCharacteristics(lancelot)

    # apply armour
    lancelot["protection"] = lancelot_stats.protection()

    # apply weapon
    lancelot["power"] = lancelot_stats.total_power()

    # apply potion to hp if exist
    lancelot["hp"] = lancelot_stats.total_hp()

    # arthur
    arthur = knights_config["arthur"]

    arthur_stats = KnightsCharacteristics(arthur)

    # apply armour
    arthur["protection"] = arthur_stats.protection()

    # apply weapon
    arthur["power"] = arthur_stats.total_power()

    # apply potion to hp if exist
    arthur["hp"] = arthur_stats.total_hp()

    # mordred
    mordred = knights_config["mordred"]

    mordred_stats = KnightsCharacteristics(mordred)

    # apply armour
    mordred["protection"] = mordred_stats.protection()

    # apply weapon
    mordred["power"] = mordred_stats.total_power()

    # apply potion to hp if exist
    mordred["hp"] = mordred_stats.total_hp()

    # red_knight
    red_knight = knights_config["red_knight"]

    red_knight_stats = KnightsCharacteristics(red_knight)

    # apply armour
    red_knight["protection"] = red_knight_stats.protection()

    # apply weapon
    red_knight["power"] = red_knight_stats.total_power()

    # apply potion to hp if exist
    red_knight["hp"] = red_knight_stats.total_hp()

    # ------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot["hp"], mordred["hp"] = Battle.one_battle(
        lancelot_stats, mordred_stats
    )

    # 2 Arthur vs Red Knight:
    arthur["hp"], red_knight["hp"] = Battle.one_battle(
        arthur_stats, red_knight_stats
    )

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
