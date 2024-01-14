from app.helpers.check import potion_check
from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon
from app.people.knight import Knight

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


def battle(knights: dict) -> dict:
    knight_class_list = []

    for knight_name, knight_specs in knights.items():
        knight = Knight(
            knight_specs["name"],
            knight_specs["power"],
            knight_specs["hp"])

        # apply armour
        for armour in knight_specs["armour"]:
            knight.apply(Armour(armour["part"], armour["protection"]))

        # apply weapon
        knight.apply(Weapon(
            knight_specs["weapon"]["name"],
            knight_specs["weapon"]["power"]
        ))

        # apply potion if exist with help of potion_check()
        if knight_specs["potion"]:
            knight.apply(Potion(*potion_check(knight_specs["potion"])))

        knight_class_list.append(knight)

    # fights
    for index in range(len(knight_class_list) - 2):
        knight_class_list[index].fight(knight_class_list[index + 2])

    return {value.name: value.hp for value in knight_class_list}


print(battle(KNIGHTS))
