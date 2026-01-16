from app.knight import Knight
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion
from app.battle import Battle


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

    for keys, value in knights_config.items():
        armours = [
            Armour(el["part"], el["protection"])
            for el in value["armour"]
        ]

        weapon = Weapon(value["weapon"]["name"], value["weapon"]["power"])
        if value.get("potion"):
            potion = Potion(
                value["potion"]["name"],
                value["potion"]["effect"].get("hp", 0),
                value["potion"]["effect"].get("power", 0),
                value["potion"]["effect"].get("protection", 0)
            )
        else:
            potion = Potion(None)
        knight = Knight(
            name=value["name"],
            hp=value["hp"],
            power=value["power"],
            armour=armours,
            weapon=weapon,
            potion=potion

        )

    for knight in Knight.knights.values():
        print(knight)

    first_battle = Battle(
        Knight.knights["Lancelot"], Knight.knights["Mordred"]
    )

    second_battle = Battle(
        Knight.knights["Arthur"], Knight.knights["Red Knight"]
    )

    first_battle.start()
    second_battle.start()

    return {knight.name: knight.hp for knight in Knight.knights.values()}


print(battle(KNIGHTS))
