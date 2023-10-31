from app.knight import Knight

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


def battle(all_knights: dict) -> dict:
    for sir in all_knights:
        Knight(all_knights[sir]["name"],
               all_knights[sir]["power"],
               all_knights[sir]["hp"],
               all_knights[sir]["armour"],
               all_knights[sir]["weapon"],
               all_knights[sir]["potion"])

    Knight.dict_knights["Lancelot"].__sub__(Knight.dict_knights["Mordred"])
    Knight.dict_knights["Mordred"].__sub__(Knight.dict_knights["Lancelot"])
    Knight.dict_knights["Arthur"].__sub__(Knight.dict_knights["Red Knight"])
    Knight.dict_knights["Red Knight"].__sub__(Knight.dict_knights["Arthur"])

    return {
        knight: Knight.dict_knights[knight].hp
        for knight in Knight.dict_knights}
