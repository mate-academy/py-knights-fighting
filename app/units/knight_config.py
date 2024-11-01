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

#  {
#             "name": "Dragon's heart",
#             "effect": {
#                 "protection": +20,
#                 "power": +10,
#                 "hp": +10,
#             }
#         }
#         base_knights_config["lancelot"]["potion"] = {
#             "name": "Magic Power",
#             "effect": {
#                 "power": +25,
#                 "hp": +10,
#             }
#         }
# >       assert battle(base_knights_config) == {
#             "Lancelot": 5,
#             "Arthur": 60,
#             "Mordred": 10,
#             "Red Knight": 0,
#         }
# E       AssertionError: assert {'Arthur': 40...ed Knight': 0} == {'Arthur': 60...ed Knight': 0}
# E         Omitting 2 identical items, use -vv to show
# E         Differing items:
# E         {'Mordred': 0} != {'Mordred': 10}
# E         {'Arthur': 40} != {'Arthur': 60}
# E         Use -v to get more diff


