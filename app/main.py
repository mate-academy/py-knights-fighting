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
            {"part": "boots", "protection": 10}
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10}
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {
            "name": "Berserk",
            "effect": {"power": 15, "hp": -5, "protection": 10},
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {"hp": 10, "power": 5},
        }
    }
}


def apply_equipment(knight: Dict[str, Any]) -> None:
    """Applies the knight's equipment: weapon, armour, and potion effects."""
    # Calculate protection from armour
    knight["protection"] = sum(a["protection"] for a in knight["armour"])

    # Add weapon power
    knight["power"] += knight["weapon"]["power"]

    # Apply potion effects if any
    if knight["potion"]:
        for effect, value in knight["potion"]["effect"].items():
            if effect == "hp":
                knight["hp"] += value
            elif effect == "power":
                knight["power"] += value
            elif effect == "protection":
                knight["protection"] += value


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """Simulates a battle between knights and returns their final HP."""
    # Apply equipment to each knight
    for knight in knights_config.values():
        apply_equipment(knight)

    # Battle: Lancelot vs Mordred
    lancelot, mordred = knights_config["lancelot"], knights_config["mordred"]
    lancelot["hp"] -= max(0, mordred["power"] - lancelot["protection"])
    mordred["hp"] -= max(0, lancelot["power"] - mordred["protection"])

    # Battle: Arthur vs Red Knight
    arthur, red_knight = knights_config["arthur"], knights_config["red_knight"]
    arthur["hp"] -= max(0, red_knight["power"] - arthur["protection"])
    red_knight["hp"] -= max(0, arthur["power"] - red_knight["protection"])

    # Return battle results
    return {
        lancelot["name"]: max(0, lancelot["hp"]),
        arthur["name"]: max(0, arthur["hp"]),
        mordred["name"]: max(0, mordred["hp"]),
        red_knight["name"]: max(0, red_knight["hp"]),
    }


print(battle(KNIGHTS))
