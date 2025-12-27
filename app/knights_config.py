from app.knights import Knight
from app.ammunition.weapon import Weapon
from app.ammunition.armour import Armour
from app.ammunition.potion import Potion

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


def dict_to_classes(dictionary: dict) -> list["Knight"]:
    """
    Transform incoming Config dictionary
    into list of 4 elements -
    each dictionary packed
    into class "Knight"
    """
    knights = []
    for knight, stats in dictionary.items():
        armour = []
        for element in stats["armour"]:
            armour.append(Armour.from_element(element))
        knight = Knight(
            name=stats["name"],
            power=stats["power"],
            hp=stats["hp"],
            armour=armour,
            weapon=Weapon(
                name=stats["weapon"]["name"],
                power=stats["weapon"]["power"]
            ),
            potion=None if stats.get("potion") is None else Potion(
                name=stats["potion"]["name"],
                effect=stats["potion"]["effect"]
            )
        )
        knights.append(knight)
    return knights
