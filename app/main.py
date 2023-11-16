from app.knights.knight import Knight


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
    dict_knights = {}
    for knight, value in knights.items():

        knight_obj = Knight(
            value["name"],
            value["power"],
            value["hp"]
        )

        Knight.prepare(
            knight_obj,
            value["armour"],
            value["weapon"],
            value["potion"]
        )
        dict_knights[knight] = knight_obj

    dict_knights["lancelot"].hp -= (dict_knights["mordred"].power
                                    - dict_knights["lancelot"].protection)
    dict_knights["mordred"].hp -= (dict_knights["lancelot"].power
                                   - dict_knights["mordred"].protection)

    # arthur vs red knight
    dict_knights["arthur"].hp -= (dict_knights["red_knight"].power
                                  - dict_knights["arthur"].protection)
    dict_knights["red_knight"].hp -= (dict_knights["arthur"].power
                                      - dict_knights["red_knight"].protection)

    for knight in dict_knights:
        if dict_knights[knight].hp < 0:
            dict_knights[knight].hp = 0

    # Return battle results:
    return {dict_knights[knight].name: dict_knights[knight].hp
            for knight in knights
            }


print(battle(KNIGHTS))
