from app.inventory.armour import Armour
from app.inventory.potion import Potion
from app.inventory.weapon import Weapon
from app.knight import Knight

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armours": [],
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
        "armours": [
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
        "armours": [
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
        "armours": [
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


def get_knights(knights_config: dict[str, dict]) -> dict[str, Knight]:
    knights = {}

    for knight_key, data in knights_config.items():
        armours = Armour.list_from_dicts(data.get("armours", []))
        potion = Potion.from_dict(data.get("potion"))

        knight = Knight(
            data["name"],
            data["power"],
            data["hp"],
            Weapon(**data["weapon"]),
            armours,
            potion
        )

        knights[knight_key] = knight

    return knights


def battle(knights_config: dict[str, dict]) -> dict[str, int]:
    # BATTLE PREPARATIONS:

    knights = get_knights(knights_config)

    # -------------------------------------------------------------------------------
    # BATTLE:

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    results = {}
    for knight1, knight2 in battles:
        results.update(knights[knight1].fight(knights[knight2]))

    # Return battle results:

    return results


print(battle(KNIGHTS))
