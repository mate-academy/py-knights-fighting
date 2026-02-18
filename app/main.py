from app.people.knights import Knight
from app.grounds.equipment_racks import Armour, Weapon, Potion
from app.grounds.battleground import Battleground


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
    knight_objects = {}

    for knight in knights_config.values():
        knight = Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            Weapon(knight["weapon"]["name"], knight["weapon"]["power"]),
            [Potion(
                knight["potion"]["name"],
                knight["potion"]["effect"].get("hp", 0),
                knight["potion"]["effect"].get("power", 0),
                knight["potion"]["effect"].get("protection", 0)
            ) if knight["potion"] else None,
                *[
                    Armour(
                        armour["part"], armour["protection"]
                    ) for armour in knight["armour"]]
            ]
        )
        knight_objects[knight.name] = knight

    for knight_obj in knight_objects.values():
        if not knight_obj.equipment_applied:
            knight_obj.apply_equip()

    bg_1 = Battleground(1)
    bg_2 = Battleground(2)
    bg_1.bg_battle(knight_objects["Lancelot"], knight_objects["Mordred"])
    bg_2.bg_battle(knight_objects["Arthur"], knight_objects["Red Knight"])

    return {
        knight_name: knight_obj.hp for knight_name,
        knight_obj in knight_objects.items()
    }
