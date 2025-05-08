KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            }
        ],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": {
            "name": "Orc Sword",
            "effect": {
            "hp": 10,
            "power": 15,
            "protection": -5
            }
                   },
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
            },
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": {"name": "Blood Blade", "effect": {
            "hp": 0, "power": 20, "protection": 3
        }
                   },
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
            },
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {"name": "Druid Drinks", "effect": {
            "hp": 40, "power": 0, "protection": 5}},
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
        "potion": {"name": "Paladin Helm", "effect": {
            "hp": 30, "power": -5, "protection": 20
        }},
    },
}
