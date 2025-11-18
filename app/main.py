from app.knight import Knight
from app.inventory.weapon import Weapon
from app.inventory.potion import Potion
from app.inventory.armor import Armor

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
    # BATTLE PREPARATIONS:
    knights = build_knights(knights_config)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


def build_knights(knights_config: dict) -> dict:
    knights = {}

    for knight_name in knights_config:
        knight = knights_config[knight_name]

        potion_data = knight.get("potion", None)
        potion_name = ""
        potion_effect = {}
        if potion_data:
            potion_name = potion_data.get("name")
            potion_effect = potion_data.get("effect")

        knights[knight_name] = Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            [Armor(armor) for armor in knight["armour"]],
            Weapon(knight["weapon"]),
            Potion(potion_name, potion_effect),
        )

    return knights


print(battle(KNIGHTS))
