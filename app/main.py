from typing import Dict, Any


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
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
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
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
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
            {"part": "breastplate", "protection": 25},
        ],
        "weapon": {
            "name": "Sword",
            "power": 45,
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


def prepare_knight(knight: Dict[str, Any]) -> None:
    """Prepare knight by applying armour, weapon and potion."""
    knight["protection"] = sum(
        piece["protection"] for piece in knight["armour"])
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        effects = knight["potion"]["effect"]
        knight["power"] += effects.get("power", 0)
        knight["protection"] += effects.get("protection", 0)
        knight["hp"] += effects.get("hp", 0)


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """Simulate battle between knights and return their remaining HP."""

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    for knight in [lancelot, arthur, mordred, red_knight]:
        prepare_knight(knight)

    lancelot_damage = max(mordred["power"] - lancelot["protection"], 0)
    mordred_damage = max(lancelot["power"] - mordred["protection"], 0)

    lancelot["hp"] = max(lancelot["hp"] - lancelot_damage, 0)
    mordred["hp"] = max(mordred["hp"] - mordred_damage, 0)

    arthur_damage = max(red_knight["power"] - arthur["protection"], 0)
    red_knight_damage = max(arthur["power"] - red_knight["protection"], 0)

    arthur["hp"] = max(arthur["hp"] - arthur_damage, 0)
    red_knight["hp"] = max(red_knight["hp"] - red_knight_damage, 0)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
