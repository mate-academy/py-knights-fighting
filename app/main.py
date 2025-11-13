from typing import Dict, Any
from .models.knight import Knight
from .battle_engine.battle import Battle

KNIGHTS = {
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


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    knights = {}
    for knight_key, knight_data in knights_config.items():
        knights[knight_key] = Knight(knight_data)

    # Define battle pairings (maintaining original tournament structure)
    battle_pairings = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    # Execute all battles
    battle_results: Dict[str, int] = {}
    for knight1_key, knight2_key in battle_pairings:
        knight1 = knights[knight1_key]
        knight2 = knights[knight2_key]

        # Create and execute battle
        battle_instance = Battle(knight1, knight2)
        single_battle_result = battle_instance.fight()

        # Merge results
        battle_results.update(single_battle_result)

    return battle_results


if __name__ == "__main__":
    # Execute the battle and print results
    result: Dict[str, int] = battle(KNIGHTS)
    print("🏰 Kingdom of Camelot - Knight Championship Results 🏰")
    print("=" * 50)
    for knight_name, hp in result.items():
        status = "⚔️  DEFEATED" if hp == 0 else f"❤️  {hp} HP"
        print(f"  {knight_name}: {status}")
