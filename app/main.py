from app.knights.knight import Knight
from app.equip.armour import Armour
from app.equip.weapon import Weapon
from app.equip.potion import Potion
from app.battle import battle_results


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
    lancelot = Knight(
        name=knights_config["lancelot"]["name"],
        power=knights_config["lancelot"]["power"],
        hp=knights_config["lancelot"]["hp"],
        armour=[
            Armour(a["protection"])
            for a in knights_config["lancelot"]["armour"]
        ],
        weapon=Weapon(knights_config["lancelot"]["weapon"]["power"]),
        potion=Potion(knights_config["lancelot"]["potion"]["effect"])
        if knights_config["lancelot"]["potion"] else None
    )
    arthur = Knight(
        name=knights_config["arthur"]["name"],
        power=knights_config["arthur"]["power"],
        hp=knights_config["arthur"]["hp"],
        armour=[
            Armour(a["protection"])
            for a in knights_config["arthur"]["armour"]
        ],
        weapon=Weapon(knights_config["arthur"]["weapon"]["power"]),
        potion=Potion(knights_config["arthur"]["potion"]["effect"])
        if knights_config["arthur"]["potion"] else None
    )
    mordred = Knight(
        name=knights_config["mordred"]["name"],
        power=knights_config["mordred"]["power"],
        hp=knights_config["mordred"]["hp"],
        armour=[
            Armour(a["protection"])
            for a in knights_config["mordred"]["armour"]
        ],
        weapon=Weapon(knights_config["mordred"]["weapon"]["power"]),
        potion=Potion(knights_config["mordred"]["potion"]["effect"])
        if knights_config["mordred"]["potion"] else None
    )
    red_knight = Knight(
        name=knights_config["red_knight"]["name"],
        power=knights_config["red_knight"]["power"],
        hp=knights_config["red_knight"]["hp"],
        armour=[
            Armour(a["protection"])
            for a in knights_config["red_knight"]["armour"]
        ],
        weapon=Weapon(knights_config["red_knight"]["weapon"]["power"]),
        potion=Potion(knights_config["red_knight"]["potion"]["effect"])
        if knights_config["red_knight"]["potion"] else None
    )
    knights = [lancelot, arthur, mordred, red_knight]
    return battle_results(knights)


print(battle(KNIGHTS))
