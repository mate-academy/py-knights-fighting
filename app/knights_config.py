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
