KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 80,
        "armour": [
            {"part": "helmet", "protection": 10},
            {"part": "boots", "protection": 5}
        ],
        "weapon": {"name": "Lance", "power": 50},
        "potion": {
            "name": "Speed Elixir",
            "effect": {
                "hp": +5,
                "power": +5
            }
        },
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "shield", "protection": 20}
        ],
        "weapon": {"name": "Excalibur", "power": 40},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 50,
        "hp": 70,
        "armour": [],
        "weapon": {"name": "Dark Blade", "power": 55},
        "potion": {
            "name": "Curse",
            "effect": {
                "power": -10,
                "hp": +20
            }
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {"part": "breastplate", "protection": 25}
        ],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5
            }
        },
    }
}
