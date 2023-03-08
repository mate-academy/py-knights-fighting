from __future__ import annotations

from app.knights.knight import Knight


# creation of knights


def knights_config(knights: dict[str, any]) -> dict:
    knights_dict = {}
    for knight_name, knight_data in knights.items():
        knight = Knight(
            knight_data["name"],
            knight_data["power"],
            knight_data["hp"],
        )
        knight.protection = 0
        knight.apply_armour(knight_data["armour"])
        knight.apply_weapon(knight_data["weapon"])
        knight.apply_potion(knight_data["potion"])
        knights_dict[knight_name] = knight
    return knights_dict


# BATTLE
def battle(knights: dict[str, any]) -> dict[str, int]:
    ready_knights = knights_config(knights)

    lancelot = ready_knights["lancelot"]
    arthur = ready_knights["arthur"]
    mordred = ready_knights["mordred"]
    red_knight = ready_knights["red_knight"]

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    red_knight.hp -= arthur.power - red_knight.protection
    arthur.hp -= red_knight.power - arthur.protection

    Knight.check_hp(lancelot)
    Knight.check_hp(mordred)
    Knight.check_hp(red_knight)
    Knight.check_hp(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


knights = {
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
