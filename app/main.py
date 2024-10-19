from app.actions.get_info import get_knights_info
from app.actions.battles import duel
from app.actions.battle_results import return_battles_results

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
                "add_some_abilities": 15,
            },
            {
                "part": "breastplate",
                "add_some_abilities": 20,
            },
            {
                "part": "boots",
                "add_some_abilities": 10,
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
                "add_some_abilities": 15,
            },
            {
                "part": "boots",
                "add_some_abilities": 10,
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
                "add_some_abilities": +10,
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
                "add_some_abilities": 25,
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


def battle(knightsconfig: dict) -> dict:
    knights = get_knights_info(knightsconfig)
    for knight in range(int(len(knightsconfig) / 2)):
        duel(knights[knight], knights[knight + 2])
    return return_battles_results(knights)


print(battle(KNIGHTS))
