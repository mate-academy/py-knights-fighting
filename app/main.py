from app.preparations.protection import count_protection
from app.preparations.power import count_power
from app.preparations.potion import count_potion
from app.battle.count_hp import count_hp


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


def battle(knightsConfig: dict) -> dict:
    knights_list = []
    for key in knightsConfig.keys():
        globals()[key] = knightsConfig[key]
        knights_list.append(globals()[key])
        count_protection(globals()[key])
        count_power(globals()[key])
        if globals()[key]["potion"] is not None:
            count_potion(globals()[key])

    count_hp(globals()["lancelot"], globals()["mordred"])
    count_hp(globals()["arthur"], globals()["red_knight"])

    return {
        globals()["lancelot"]["name"]: globals()["lancelot"]["hp"],
        globals()["arthur"]["name"]: globals()["arthur"]["hp"],
        globals()["mordred"]["name"]: globals()["mordred"]["hp"],
        globals()["red_knight"]["name"]: globals()["red_knight"]["hp"],
    }


print(battle(KNIGHTS))
