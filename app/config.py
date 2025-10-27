# app/config.py

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 50,
        "hp": 85,
        "armour": [
            {"part": "helmet", "protection": 10},
            {"part": "boots", "protection": 5},
        ],
        "weapon": {"name": "Lance", "power": 40},
        "potion": {
            "name": "Holy Water",
            "effect": {
                "hp": +5,
                "power": +10,
            },
        },
    },

    "arthur": {
        "name": "Arthur",
        "power": 55,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 20},
        ],
        "weapon": {"name": "Excalibur", "power": 50},
        "potion": {
            "name": "Royal Oath",
            "effect": {
                "hp": +10,
                "power": +5,
                "protection": +5,
            },
        },
    },

    "mordred": {
        "name": "Mordred",
        "power": 60,
        "hp": 95,
        "armour": [
            {"part": "shoulder", "protection": 15},
            {"part": "gauntlets", "protection": 5},
        ],
        "weapon": {"name": "Dark Blade", "power": 35},
        "potion": {
            "name": "Curse",
            "effect": {
                "hp": -5,
                "power": +15,
                "protection": 0,
            },
        },
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
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}
