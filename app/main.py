from typing import Dict, Any
from .knight import Knight
from .battle import simulate_fight


KNIGHTS: Dict[str, Dict[str, Any]] = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10}
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10}
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
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
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """
    Orchestrates the two required knight battles using the Knight class 
    and modular logic.
    """
    
    knight_instances = {
        key: Knight(data) for key, data in knights_config.items()
    }

    battle_pairs = [
        (knight_instances["lancelot"], knight_instances["mordred"]),
        (knight_instances["arthur"], knight_instances["red_knight"]),
    ]

    for knight_a, knight_b in battle_pairs:
        simulate_fight(knight_a, knight_b)
    
    return {
        name: instance.hp 
        for name, instance in knight_instances.items()
    }
