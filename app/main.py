from copy import deepcopy

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


def prepare_to_fight(knight: dict) -> None:
    """Apply all effects (armor, weapon, potion) to a knight."""
    # Initialize protection
    knight["protection"] = 0

    # Apply armor
    for armor_piece in knight["armour"]:
        knight["protection"] += armor_piece["protection"]

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if exists
    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            if stat == "protection":
                knight["protection"] += value
            else:
                knight[stat] = max(0, knight[stat] + value)


def to_battle(knight1: dict, knight2: dict) -> None:
    """Process a battle between two knights."""
    # Calculate damage
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])

    # Ensure HP doesn't go below 0
    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])

    # -------------------------------------------------------------------------------
    # BATTLE:


def battle(knightsconfig: dict) -> dict:
    knights = {
        name: deepcopy(knight)
        for name, knight in knightsconfig.items()
    }

    for knight_name, knight in knights.items():
        print(knight)
        prepare_to_fight(knight)

    # Process battles
    to_battle(knights["lancelot"], knights["mordred"])
    to_battle(knights["arthur"], knights["red_knight"])

    # Return battle results:
    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }


print(battle(KNIGHTS))
