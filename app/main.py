from app.knight.knight_class import Knight
from app.battle.battle_knights import single_battle

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


def parse_knights(knights_dict: dict) -> dict:
    knights_object = {knights_name: Knight(
        name=knights_data["name"],
        power=knights_data["power"],
        hp=knights_data["hp"],
        armour=knights_data["armour"],
        weapon=knights_data["weapon"],
        potion=knights_data["potion"])
        for knights_name, knights_data in knights_dict.items()}
    return knights_object


def battle(knights_dict: dict) -> dict:
    knights_instances = parse_knights(knights_dict)
    lancelot = knights_instances.get("lancelot")
    arthur = knights_instances.get("arthur")
    mordred = knights_instances.get("mordred")
    red_knight = knights_instances.get("red_knight")
    first_battle = single_battle(lancelot, mordred)
    first_battle.update(single_battle(arthur, red_knight))
    return first_battle


print(battle(KNIGHTS))
