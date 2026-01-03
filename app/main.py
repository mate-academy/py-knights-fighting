from app.knights.knight import Knight
from app.battle.preparation import prepare
from app.battle.battle_result import get_battle_results


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


def battle(knight_config: dict) -> dict:
    lancelot = Knight(
        knight_config["lancelot"]["name"],
        knight_config["lancelot"]["power"],
        knight_config["lancelot"]["hp"],
        knight_config["lancelot"]["armour"],
        knight_config["lancelot"]["weapon"],
        knight_config["lancelot"]["potion"])
    arthur = Knight(
        knight_config["arthur"]["name"],
        knight_config["arthur"]["power"],
        knight_config["arthur"]["hp"],
        knight_config["arthur"]["armour"],
        knight_config["arthur"]["weapon"],
        knight_config["arthur"]["potion"])
    mordred = Knight(
        knight_config["mordred"]["name"],
        knight_config["mordred"]["power"],
        knight_config["mordred"]["hp"],
        knight_config["mordred"]["armour"],
        knight_config["mordred"]["weapon"],
        knight_config["mordred"]["potion"])
    red_knight = Knight(
        knight_config["red_knight"]["name"],
        knight_config["red_knight"]["power"],
        knight_config["red_knight"]["hp"],
        knight_config["red_knight"]["armour"],
        knight_config["red_knight"]["weapon"],
        knight_config["red_knight"]["potion"])

    prepare(lancelot)
    prepare(arthur)
    prepare(mordred)
    prepare(red_knight)

    return get_battle_results(lancelot, mordred) | \
        get_battle_results(arthur, red_knight)
