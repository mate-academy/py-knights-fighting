from app.battle import logic_of_battle
from app.knights.config import Knights


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


def battle(knightsconfig : dict) -> dict:
    # BATTLE PREPARATIONS:

    # create instances
    knight_instance = []
    for value in knightsconfig.values():
        knight_instance.append(Knights(value["name"], value["power"],
                                       value["hp"], value["armour"],
                                       value["weapon"], value["potion"])
                               )

    # knights are equipmented
    for knight in knight_instance:
        knight.equipment_knight()
        # print(knight.name_knight, knight.stats)

    # BATTLE:
    logic_of_battle.battle_begin(knight_instance[0], knight_instance[2])
    logic_of_battle.battle_begin(knight_instance[1], knight_instance[3])

    # Return battle results:
    result = {}
    for knight in knight_instance:
        result[knight.name_knight] = knight.stats["hp"]

    return result


print(battle(KNIGHTS))
