"""
Docstring for Kodree.github_tasks.py-knights-fighting.app.main

Main application file for knights fighting simulation.
"""

from app.knight import ArmourPiece, Weapon, Potion, Knight


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


# Function to simulate fights between knights
def fight(knight1: Knight, knight2: Knight) -> dict[str, int]:
    return {
        knight1.name: max(
            0,
            knight1.hp - (knight2.power - knight1.protection)
        ),
        knight2.name: max(
            0,
            knight2.hp - (knight1.power - knight2.protection)
        )
    }


def battle(knightsconfig: dict) -> dict[str, int]:
    # Initialize knights from configuration
    knights_obj: dict[str, Knight] = {}
    for key, config in knightsconfig.items():
        knights_obj[key] = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=[
                ArmourPiece(**armour) for armour in config["armour"]
            ],
            weapon=Weapon(**config["weapon"]),
            potion=Potion(**config["potion"]) if config["potion"] else None
        )

    # BATTLE PREPARATIONS:
    for knight in knights_obj.values():
        knight.prepare_for_battle()

    # SIMULATE BATTLES:
    # 1 Lancelot vs Mordred:
    fight_results = fight(
        knights_obj["lancelot"], knights_obj["mordred"]
    )
    # 2 Arthur vs Red Knight:
    fight_results.update(
        fight(knights_obj["arthur"], knights_obj["red_knight"])
    )

    # Return the resulting knights with their updated HP
    return fight_results
