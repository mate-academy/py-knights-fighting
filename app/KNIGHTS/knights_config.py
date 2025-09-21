from app.game.armour import Armour
from app.game.Weapon import Weapon
from app.game.Potion import Potion

slem = Armour("slem", 20)
bronia = Armour("bronia", 45)

metal_sword = Weapon("Metal Sword", 50)
sword = Weapon("Sword", 45)

blessing = Potion("Blessing", {"hp": 10, "power": 5})

# app/KNIGHTS/knights_config.py

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [
            {"part": "slem", "protection": 20},
            {"part": "bronia", "protection": 45},
        ],
        "weapon": {"name": "Metal Sword", "power": 50},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "shoulder", "protection": 15},
        ],
        "weapon": {"name": "Excalibur", "power": 60},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 55,
        "hp": 90,
        "armour": [
            {"part": "helmet", "protection": 20},
        ],
        "weapon": {"name": "Dark Sword", "power": 40},
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
            "effect": {"hp": 10, "power": 5},
        },
    },
}
