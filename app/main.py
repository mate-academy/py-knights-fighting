from app.knights.apply_armour import Armour
from app.knights.apply_potion import Potion

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


def battle(KnightsConfig):

    # preaparations
    # list of lists [name, power, hp, protection]

    knights = []

    for key, value in KnightsConfig.items():
        # list [name, power, hp, protection)
        knight_list = []

        knight = KnightsConfig[key]

        knight_list.append(knight["name"])

        knight_list.append(knight["power"] + knight["weapon"]["power"])

        knight_list.append(knight["hp"])

        knight_list.append(Armour.app_armour(knight["armour"]))

        if knight["potion"] is not None:
            knight_list[1], knight_list[2], knight_list[3] = Potion.app_potion(
                knight["potion"], knight_list[1],
                knight_list[2], knight_list[3])

        knights.append(knight_list)
        print(knights)
    # -------------------------------------------------------------------------------
    # list result hp_after_fighting
    result = []
    for i in range(2):
        result.append(knights[i][2] - knights[i + 2][1] + knights[i][3])
        print(result)
        result.append(knights[i + 2][2] - knights[i][1] + knights[i + 2][3])

    for j in range(len(KnightsConfig)):
        if result[j] <= 0:
            result[j] = 0

    return {
        knights[0][0]: result[0],
        knights[1][0]: result[2],
        knights[2][0]: result[1],
        knights[3][0]: result[3],
    }
