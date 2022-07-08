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


def battle(KnightsConfig):

    # Preaparations
    # list of lists [name, power, hp, protection]
    Knights = []

    for k, v in KnightsConfig.items():
        # list [name, power, hp, protection)
        Knight = []

        knight = KnightsConfig[k]

        Knight.append(knight["name"])

        Knight.append(knight["power"] + knight["weapon"]["power"])

        Knight.append(knight["hp"])

        Knight.append(Armour.app_armour(knight["armour"]))

        if knight["potion"] is not None:
            Knight[1], Knight[2], Knight[3] = Potion.app_potion(
                knight["potion"], Knight[1], Knight[2], Knight[3])

        Knights.append(Knight)
        print(Knights)
    # -------------------------------------------------------------------------------
    # list result hp_after_fighting
    result = []
    for i in range(2):
        result.append(Knights[i][2] - Knights[i + 2][1] + Knights[i][3])
        print(result)
        result.append(Knights[i + 2][2] - Knights[i][1] + Knights[i + 2][3])

    for j in range(4):
        if result[j] <= 0:
            result[j] = 0

    return {
        Knights[0][0]: result[0],
        Knights[1][0]: result[2],
        Knights[2][0]: result[1],
        Knights[3][0]: result[3],
    }
