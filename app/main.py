from app.knights import Knight
from app.battle import Battle


lancelot = Knight(
    "Lancelot",
    35,
    100,
    [],
    {
        "name": "Metal Sword",
        "power": 50,
    },
    None)

arthur = Knight(
    "Arthur",
    45,
    75,
    [
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
    {
        "name": "Two-handed Sword",
        "power": 55,
    },
    None)

mordred = Knight(
    "Mordred",
    30,
    90,
    [
        {
            "part": "breastplate",
            "protection": 15,
        },
        {
            "part": "boots",
            "protection": 10,
        }
    ],
    {
        "name": "Poisoned Sword",
        "power": 60,
    },
    {
        "name": "Berserk",
        "effect": {
            "power": +15,
            "hp": -5,
            "protection": +10
        }
    })
red_knight = Knight(
    "Red Knight",
    40,
    70,
    [
        {
            "part": "breastplate",
            "protection": 25,
        }
    ],
    {
        "name": "Sword",
        "power": 45
    },
    {
        "name": "Blessing",
        "effect": {
            "hp": +10,
            "power": +5,
        }
    })

knights = [lancelot, arthur, mordred, red_knight]


def battle(knights_conf: list) -> dict:
    for knight in knights_conf:
        Knight.preparation(knight)

    Battle.knights_battle(lancelot, mordred)
    Battle.knights_battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(knights))
