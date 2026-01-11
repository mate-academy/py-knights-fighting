from app.knight.knight import Knight
from app.knight.preparations import prepare_knight_to_battle
from app.knight.battle import battling


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


def battle(knightsconfig: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight.create_knight(knightsconfig["lancelot"])
    prepare_knight_to_battle(lancelot)

    # arthur
    arthur = Knight.create_knight(knightsconfig["arthur"])
    prepare_knight_to_battle(arthur)

    # mordred
    mordred = Knight.create_knight(knightsconfig["mordred"])
    prepare_knight_to_battle(mordred)

    # red_knight
    red_knight = Knight.create_knight(knightsconfig["red_knight"])
    prepare_knight_to_battle(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battling(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    battling(arthur, red_knight)

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in (lancelot, mordred, arthur, red_knight)
    }


print(battle(KNIGHTS))
