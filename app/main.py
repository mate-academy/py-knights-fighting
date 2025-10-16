from typing import Dict, Any

from .knight import Knight
from .battle import Battle


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
            },
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
            },
        },
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
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    lancelot = Knight(**knights_config["lancelot"])
    mordred = Knight(**knights_config["mordred"])
    arthur = Knight(**knights_config["arthur"])
    red_knight = Knight(**knights_config["red_knight"])

    first_battle = Battle(lancelot, mordred)
    first_battle.prepare_for_fight()

    second_battle = Battle(arthur, red_knight)
    second_battle.prepare_for_fight()

    first_battle_result = first_battle.fight()
    second_battle_result = second_battle.fight()

    return {
        **first_battle_result,
        **second_battle_result,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
