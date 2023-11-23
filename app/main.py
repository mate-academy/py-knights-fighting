from typing import Dict, Any


def apply_preparations(knight: Dict[str, Any]) -> None:
    knight["protection"] = sum(
        armor["protection"] for armor in knight["armour"]
    )

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        knight["power"] += knight["potion"]["effect"].get("power", 0)
        knight["protection"] += knight["potion"]["effect"].get("protection", 0)
        knight["hp"] += knight["potion"]["effect"].get("hp", 0)


def apply_battle(knight1: dict, knight2: dict) -> None:
    damage1 = max(0, knight2["power"] - knight1["protection"])
    damage2 = max(0, knight1["power"] - knight2["protection"])

    knight1["hp"] -= damage1
    knight2["hp"] -= damage2

    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knights_config: dict) -> dict:
    for knight in knights_config.values():
        apply_preparations(knight)

    apply_battle(knights_config["lancelot"], knights_config["mordred"])
    apply_battle(knights_config["arthur"], knights_config["red_knight"])

    return {knight["name"]: knight["hp"] for knight in knights_config.values()}


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
                "power": 15,
                "hp": -5,
                "protection": 10,
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
                "hp": 10,
                "power": 5,
            }
        }
    }
}

print(battle(KNIGHTS))
