KNIGHTS = {
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": 10,
                "power": 5
            }
        },
    },
    "mordred": {
        "name": "Mordred",
        "power": 35,
        "hp": 90,
        "armour": [{"part": "helmet", "protection": 15}],
        "weapon": {"name": "Axe", "power": 30},
        "potion": {"name": "Curse", "effect": {"power": -5}},
    },
    "lancelot": {
        "name": "Lancelot",
        "power": 50,
        "hp": 85,
        "armour": [{
            "part": "boots",
            "protection": 10
        }, {
            "part": "helmet",
            "protection": 5
        }],
        "weapon": {"name": "Lance", "power": 40},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 60,
        "hp": 80,
        "armour": [],
        "weapon": {"name": "Excalibur", "power": 50},
        "potion": {
            "name": "Elixir",
            "effect": {
                "hp": 15, "protection": 10
            }
        },
    },
}
