from typing import Dict, Any


def apply_armour(knight: Dict[str, Any]) -> int:
    """Calculate total armour protection for a knight."""
    return sum(piece["protection"] for piece in knight["armour"])


def apply_weapon(knight: Dict[str, Any]) -> int:
    """Calculate total power with the weapon applied."""
    return knight["power"] + knight["weapon"]["power"]


def apply_potion(knight: Dict[str, Any]) -> None:
    """Apply potion effects to the knight, if any."""
    if knight["potion"]:
        effect = knight["potion"]["effect"]
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)


def prepare_knight(knight: Dict[str, Any]) -> Dict[str, Any]:
    """Prepare knight with armour, weapon, and potion."""
    knight["protection"] = apply_armour(knight)
    knight["power"] = apply_weapon(knight)
    apply_potion(knight)
    return knight


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """Simulate a battle between knights."""
    # Prepare all knights
    lancelot = prepare_knight(knights_config["lancelot"])
    arthur = prepare_knight(knights_config["arthur"])
    mordred = prepare_knight(knights_config["mordred"])
    red_knight = prepare_knight(knights_config["red_knight"])

    # Battle 1: Lancelot vs Mordred
    lancelot["hp"] -= max(0, mordred["power"] - lancelot["protection"])
    mordred["hp"] -= max(0, lancelot["power"] - mordred["protection"])

    # Ensure HP doesn't drop below zero
    lancelot["hp"] = max(0, lancelot["hp"])
    mordred["hp"] = max(0, mordred["hp"])

    # Battle 2: Arthur vs Red Knight
    arthur["hp"] -= max(0, red_knight["power"] - arthur["protection"])
    red_knight["hp"] -= max(0, arthur["power"] - red_knight["protection"])

    arthur["hp"] = max(0, arthur["hp"])
    red_knight["hp"] = max(0, red_knight["hp"])

    # Return battle results
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


# Example usage
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

if __name__ == "__main__":
    print(battle(KNIGHTS))
