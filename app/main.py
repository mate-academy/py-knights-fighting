from app.knights import Knight
from app.to_fight import fight

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
        "name": "Artur",
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


def battle(knightsconfig: dict) -> dict:
    list_knights = []
    dict_knight = {}
    knight_name = []
    result_fight = {}
    for knights in knightsconfig.items():
        list_knights.append(Knight(knights[1]))
        knight_name.append(Knight(knights[1]).name)
    for knight_instance in list_knights:
        dict_knight[knight_instance.name] = knight_instance.knight_stats()
    for vs in range(2):
        result_fight[knight_name[vs]] = fight(dict_knight[knight_name[vs]],
                                              dict_knight[knight_name[vs + 2]])
    for vs in range(2, 4):
        result_fight[knight_name[vs]] = fight(dict_knight[knight_name[vs]],
                                              dict_knight[knight_name[vs - 2]])
    return result_fight


print(battle(KNIGHTS))
