

KNIGHTS = {
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {"name": "Blessing", "effect": {"hp": +10, "power": +5}},
    },
    "lancelot": {
        "name": "Lancelot",
        "power": 60,
        "hp": 90,
        "armour": [{"part": "helmet", "protection": 20}],
        "weapon": {"name": "Spear", "power": 35},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 55,
        "hp": 95,
        "armour": [],
        "weapon": {"name": "Excalibur", "power": 50},
        "potion": {"name": "Shield", "effect": {"protection": 10}},
    },
    "mordred": {
        "name": "Mordred",
        "power": 65,
        "hp": 85,
        "armour": [
            {"part": "boots", "protection": 10},
            {"part": "gloves", "protection": 5},
        ],
        "weapon": {"name": "Axe", "power": 30},
        "potion": {"name": "Curse", "effect": {"hp": -10, "protection": -5}},
    },
}
