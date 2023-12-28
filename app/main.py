from typing import Dict


KNIGHTS: Dict[str, Dict[str, dict]] = {
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
                "power": +15,
                "hp": -5,
                "protection": +10,
            },
        },
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
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def apply_effects(knight: dict) -> None:
    # apply armour
    knight["protection"] = sum(
        armor["protection"] for armor in knight["armour"]
    )

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    if knight["potion"] is not None:
        effect = knight["potion"]["effect"]
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    # BATTLE PREPARATIONS:

    # Apply effects to each knight
    for knight_name, knight in knights_config.items():
        apply_effects(knight)

    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights_config["lancelot"]["hp"] -= (
        knights_config["mordred"]["power"]
        - knights_config["lancelot"]["protection"]
    )
    knights_config["mordred"]["hp"] -= (
        knights_config["lancelot"]["power"]
        - knights_config["mordred"]["protection"]
    )

    # check if someone fell in battle
    for knight_name, knight in knights_config.items():
        knight["hp"] = max(0, knight["hp"])

    # 2 Arthur vs Red Knight:
    knights_config["arthur"]["hp"] -= (
        knights_config["red_knight"]["power"]
        - knights_config["arthur"]["protection"]
    )
    knights_config["red_knight"]["hp"] -= (
        knights_config["arthur"]["power"]
        - knights_config["red_knight"]["protection"]
    )

    # check if someone fell in battle
    for knight_name, knight in knights_config.items():
        knight["hp"] = max(0, knight["hp"])

    # Return battle results:
    return {knight["name"]: knight["hp"] for knight in knights_config.values()}


print(battle(KNIGHTS))
