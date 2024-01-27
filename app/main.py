from app.items.weapon import Weapon
from app.items.potion import Potion
from app.items.armour import Armour
from app.participants.knight import Knight

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
    all_knights = {one_knight: Knight(
        name=knights[one_knight]["name"],
        power=knights[one_knight]["power"],
        hp=knights[one_knight]["hp"],
        armour=[Armour(part=armour["part"],
                       protection=armour["protection"])
                for armour in knights[one_knight]["armour"]],
        weapon=Weapon(name=knights[one_knight]["weapon"]["name"],
                      power=knights[one_knight]["weapon"]["power"]),
        potion=None if knights[one_knight].get("potion") is None else
        Potion(name=knights[one_knight]["potion"]["name"],
               effect=knights[one_knight]["potion"]["effect"])
    ) for one_knight in knights}

    # 1 Lancelot vs Mordred:
    all_knights["lancelot"] - all_knights["mordred"]

    # 2 Arthur vs Red Knight:
    all_knights["arthur"] - all_knights["red_knight"]

    # Return battle results:
    return {
        all_knights["lancelot"].name: all_knights["lancelot"].hp,
        all_knights["arthur"].name: all_knights["arthur"].hp,
        all_knights["mordred"].name: all_knights["mordred"].hp,
        all_knights["red_knight"].name: all_knights["red_knight"].hp,
    }


print(battle(KNIGHTS))
