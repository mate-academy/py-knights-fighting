KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "hp": 90,
        "power": 60,
        "armour": [
            {"part": "helmet", "protection": 10},
            {"part": "shield", "protection": 20},
        ],
        "weapon": {"name": "Spear", "power": 50},
        "potion": None,
    },

    "mordred": {
        "name": "Mordred",
        "hp": 100,
        "power": 70,
        "armour": [
            {"part": "breastplate", "protection": 25},
        ],
        "weapon": {"name": "Axe", "power": 40},
        "potion": {
            "name": "Rage",
            "effect": {"power": 10, "hp": -5},
        },
    },

    "arthur": {
        "name": "Arthur",
        "hp": 80,
        "power": 50,
        "armour": [],
        "weapon": {"name": "Excalibur", "power": 60},
        "potion": None,
    },

    "red_knight": {
        "name": "Red Knight",
        "hp": 70,
        "power": 40,
        "armour": [
            {"part": "breastplate", "protection": 25},
        ],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {"hp": 10, "power": 5},
        },
    },
}
