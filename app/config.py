KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 30,
        "hp": 80,
        "armour": [
            {"part": "helmet", "protection": 10},
            {"part": "boots", "protection": 5},
        ],
        "weapon": {"name": "Lance", "power": 40},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 35,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 20},
        ],
        "weapon": {"name": "Excalibur", "power": 50},
        "potion": {
            "name": "Strength",
            "effect": {"hp": 0, "power": 10, "protection": 5},
        },
    },
    "mordred": {
        "name": "Mordred",
        "power": 40,
        "hp": 70,
        "armour": [],
        "weapon": {"name": "Axe", "power": 45},
        "potion": {
            "name": "Weakness",
            "effect": {"hp": -10, "power": -5, "protection": 0},
        },
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
            "effect": {"hp": 10, "power": 5, "protection": 0},
        },
    },
}
