from app.people.knight import Knight
from app.battle_arena.equipped_knight import EquippedKnight
from app.battle_arena.battle import Battle


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


def battle(knights: dict) -> dict:
    """I still don't like this hardcode,
    but I don't know how to make it better.
    It would be easier if I knew how to work
    with the API in Python, but I don't, or if
    the knights just fought the next person on
    the list. In any case, I look forward to your comments"""
    knights_obj_list = Knight.battle(knights)
    lancelot = knights_obj_list.get("lancelot")
    mordred = knights_obj_list.get("mordred")
    arthur = knights_obj_list.get("arthur")
    red_knight = knights_obj_list.get("red_knight")
    equipped_lancelot = EquippedKnight(lancelot)
    equipped_arthur = EquippedKnight(arthur)
    equipped_mordred = EquippedKnight(mordred)
    equipped_red_knight = EquippedKnight(red_knight)
    return Battle.battle(equipped_lancelot,
                         equipped_mordred,
                         equipped_arthur,
                         equipped_red_knight)


print(battle(KNIGHTS))
