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

    armored_knights = {}

    for knight, knight_properties in knights_config.items():
        knight_stats = KnightsCharacteristics(knight_properties)

        armored_knights[knight_properties["name"]] = knight_stats

    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot_stats = armored_knights["Lancelot"]
    mordred_stats = armored_knights["Mordred"]
    lancelot_stats.hp, mordred_stats.hp = Battle.one_battle(
        lancelot_stats, mordred_stats
    )

    # 2 Arthur vs Red Knight:
    arthur_stats = armored_knights["Arthur"]
    red_knight_stats = armored_knights["Red Knight"]
    arthur_stats.hp, red_knight_stats.hp = Battle.one_battle(
        arthur_stats, red_knight_stats
    )

    # Return battle results:
    return {
        lancelot_stats.name: lancelot_stats.hp,
        arthur_stats.name: arthur_stats.hp,
        mordred_stats.name: mordred_stats.hp,
        red_knight_stats.name: red_knight_stats.hp,
    }


print(battle(KNIGHTS))
