from typing import Dict

from app.knight import Knight

Lancelot_data = {
    "name": "Lancelot",
    "power": 35,
    "hp": 100,
    "weapon": {"name": "Metal Sword", "power": 50}
}

Arthur_data = {
    "name": "Arthur",
    "power": 45,
    "hp": 75,
    "armour": [
        {"part": "helmet", "protection": 15},
        {"part": "breastplate", "protection": 20},
        {"part": "boots", "protection": 10}
    ],
    "weapon": {"name": "Two-handed Sword", "power": 55}
}

Mordred_data = {
    "name": "Mordred",
    "power": 30,
    "hp": 90,
    "armour": [
        {"part": "breastplate", "protection": 15},
        {"part": "boots", "protection": 10}
    ],
    "weapon": {"name": "Poisoned Sword", "power": 60},
    "potion": {
        "name": "Berserk",
        "effect": {"power": 15, "hp": -5, "protection": 10}
    }
}

Red_knight_data = {
    "name": "Red Knight",
    "power": 40,
    "hp": 70,
    "armour": [{"part": "breastplate", "protection": 25}],
    "weapon": {"name": "Sword", "power": 45},
    "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}}
}

Lancelot = Knight(**Lancelot_data)
Arthur = Knight(**Arthur_data)
Mordred = Knight(**Mordred_data)
Red_knight = Knight(**Red_knight_data)

knights_config: Dict[str, Knight] = {
    "Lancelot": Lancelot,
    "Arthur": Arthur,
    "Mordred": Mordred,
    "Red_knight": Red_knight
}
