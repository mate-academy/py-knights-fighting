from app.arena.battle import knights_preparation, start_battle, \
    get_battle_results
from app.fighters.knight import Knight

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


def find_knight_by_name(knights: list[Knight], name: str) -> Knight | None:
    for knight in knights:
        if knight.name == name:
            return knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights_obj_list = Knight.create_knight_objects(knights_config)
    prepared_knights = knights_preparation(knights_obj_list)

    battle_lists = []
    lancelot = find_knight_by_name(prepared_knights, "Lancelot")
    mordred = find_knight_by_name(prepared_knights, "Mordred")

    battle_lists.append(start_battle(lancelot, mordred))

    arthur = find_knight_by_name(prepared_knights, "Arthur")
    red_knight = find_knight_by_name(prepared_knights, "Red Knight")

    battle_lists.append(start_battle(arthur, red_knight))

    return get_battle_results(battle_lists)
