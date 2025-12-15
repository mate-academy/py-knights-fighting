from typing import Dict, Any

KNIGHTS: Dict[str, Dict[str, Any]] = {
    "lancelot": {
        "name": "Lancelot",
        "power": 50,
        "hp": 90,
        "armour": [
            {"part": "helmet", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Excalibur", "power": 50},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 60,
        "hp": 85,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Longsword", "power": 40},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 55,
        "hp": 95,
        "armour": [
            {"part": "helmet", "protection": 10},
            {"part": "breastplate", "protection": 15},
        ],
        "weapon": {"name": "Poisoned Sword", "power": 45},
        "potion": None,
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {"part": "breastplate", "protection": 25},
        ],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {"hp": +10, "power": +5},
        },
    },
}
