from typing import Dict, Any

KNIGHTS = {
    "ukraine": {
        "name": "Україна",
        "power": 1000,
        "hp": 1000,
        "armour": [{"part": "щит", "protection": 1000}],
        "weapon": {"name": "Потужний меч", "power": 1000},
        "potion": {
            "name": "Незламність",
            "effect": {"hp": 1000, "power": 1000, "protection": 1000},
        },
    },
    "china": {
        "name": "Китай",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50},
        "potion": None,
    },
    "russia": {
        "name": "Росія",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "iran": {
        "name": "Іран",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {
            "name": "Berserk",
            "effect": {"power": +15, "hp": -5, "protection": +10},
        },
    },
}


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:

    for knight_key, knight_data in knights_config.items():
        knight_data["protection"] = sum(
            armour["protection"] for armour in knight_data["armour"]
        )
        knight_data["power"] += knight_data["weapon"]["power"]
        if knight_data["potion"] is not None:
            knight_data["hp"] += knight_data["potion"]["effect"].get("hp", 0)
            knight_data["power"] +=\
                knight_data["potion"]["effect"].get("power", 0)
            knight_data["protection"] += knight_data["potion"]["effect"].get(
                "protection", 0
            )

    knights_config["ukraine"]["hp"] -= (
        knights_config["iran"]["power"]
        - knights_config["ukraine"]["protection"]
    )
    knights_config["iran"]["hp"] -= (
        knights_config["ukraine"]["power"]
        - knights_config["iran"]["protection"]
    )

    knights_config["china"]["hp"] -= (
        knights_config["russia"]["power"]
        - knights_config["china"]["protection"]
    )
    knights_config["russia"]["hp"] -= (
        knights_config["china"]["power"]
        - knights_config["russia"]["protection"]
    )

    for knight in ["ukraine", "china", "russia", "iran"]:
        if knights_config[knight]["hp"] < 0:
            knights_config[knight]["hp"] = 0

    return {
        knights_config["ukraine"]["name"]: knights_config["ukraine"]["hp"],
        knights_config["china"]["name"]: knights_config["china"]["hp"],
        knights_config["russia"]["name"]: knights_config["russia"]["hp"],
        knights_config["iran"]["name"]: knights_config["iran"]["hp"],
    }
