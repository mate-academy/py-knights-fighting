from app.knight_info import Weapon, Knight
from app.battle import fight


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


def battle(knights_dict: dict) -> dict:
    fight_dict = {}
    for key, value in knights_dict.items():
        weapon_d = Weapon(
            name=value["weapon"]["name"],
            power=value["weapon"]["power"]
        )
        fight_dict[key] = Knight(
            name=value["name"],
            power=value["power"],
            hp=value["hp"],
            weapon=weapon_d,
            armour=value["armour"],
            potion=value["potion"]
        )
    for knight in fight_dict.values():
        knight.prepare_for_battle()

    # 1 Lancelot vs Mordred:
    fight(fight_dict["lancelot"], fight_dict["mordred"])

    # 2 Arthur vs Red Knight:
    fight(fight_dict["arthur"], fight_dict["red_knight"])

    results = {}
    for knight in fight_dict.values():
        results[knight.name] = knight.hp
    return results
