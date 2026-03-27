from typing import Any

from app.models.knight import Knight

KNIGHTS: dict[
    str,
    dict[str, str | int | list[Any] | dict[str, str | int] | None]

    | dict[str, str | int | list[dict[str, str | int]]
                    | dict[str, str | int] | None]
    | dict[str, str | int | list[dict[str, str | int]]]
    | dict[str, str | int]
    | dict[str, str | dict[str, int]]
] = {
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


def combat(knights_config: dict) -> dict[str, int]:
    knight_dict = {}
    for knight in knights_config:
        knight_class = Knight(
            name=knights_config[knight]["name"],
            power=knights_config[knight]["power"],
            hp=knights_config[knight]["hp"],
            armour=knights_config[knight]["armour"],
            weapon=knights_config[knight]["weapon"],
            potion=knights_config[knight]["potion"]
        )

        knight_class.prepare_for_battle()
        knight_dict[knight] = knight_class

    lancelot = knight_dict["lancelot"]
    mordred = knight_dict["mordred"]
    lancelot.fight(mordred)

    arthur = knight_dict["arthur"]
    red_knight = knight_dict["red_knight"]
    arthur.fight(red_knight)

    # Return fight results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(combat(KNIGHTS))
