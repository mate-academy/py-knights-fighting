from app.models.knight import Knight
from app.models.equipment import Weapon, Armour, Potion


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


def create_knight_from_data(knight_data: dict) -> Knight:
    knight = Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"]
    )

    armour_objects = []
    for armour_data in knight_data["armour"]:
        armour = Armour(
            part=armour_data["part"],
            protection=armour_data["protection"]
        )
        armour_objects.append(armour)
    knight.equip_armor(armour_objects)

    weapon = Weapon(
        knight_data["weapon"]["name"],
        knight_data["weapon"]["power"]
    )
    knight.equip_weapon(weapon)

    if knight_data["potion"]:
        potion = Potion(
            knight_data["potion"]["name"],
            knight_data["potion"]["effect"]
        )
        knight.equip_potion(potion)

    return knight


def create_all_knights(knights_dict: dict) -> dict[str, Knight]:
    knights = {}
    for knight_key, knight_data in knights_dict.items():
        knights[knight_key] = create_knight_from_data(knight_data)

    return knights
