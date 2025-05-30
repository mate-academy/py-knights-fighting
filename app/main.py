from typing import Dict
from app.squire import create_knight_from_config
from battle.battle_engine import simulate_duel

KNIGHTS_CONFIG = {
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
            }
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
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
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

def battle(knights_config: Dict) -> Dict[str, int]:
    knights = {
        name: create_knight_from_config(name, config)
        for name, config in knights_config.items()
    }

    duel_pairs = [
        (knights["lancelot"], knights["mordred"]),
        (knights["arthur"], knights["red_knight"]),
    ]

    battle_results = {}
    for knight1, knight2 in duel_pairs:
        result = simulate_duel(knight1, knight2)
        battle_results.update(result)

    return battle_results

if __name__ == "__main__":
    results = battle(KNIGHTS_CONFIG)
    print("\n--- Результати битви ---")
    for name, hp in results.items():
        print(f"{name}: {hp} HP")
