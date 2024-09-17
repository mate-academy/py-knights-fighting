from app.warior import Warior

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


def fight(warior1: Warior, warior2: Warior) -> dict:
    warior1.hp -= warior2.power - warior1.protection
    warior2.hp -= warior1.power - warior2.protection

    if warior1.hp <= 0:
        warior1.hp = 0

    if warior2.hp <= 0:
        warior2.hp = 0

    return {
        warior1.name: warior1.hp,
        warior2.name: warior2.hp,
    }


def battle(knights_config: dict) -> dict:
    lancelot = Warior(knights_config["lancelot"])
    mordred = Warior(knights_config["mordred"])
    arthur = Warior(knights_config["arthur"])
    red_knight = Warior(knights_config["red_knight"])

    result1 = fight(lancelot, mordred)
    result2 = fight(arthur, red_knight)

    return {**result1, **result2}


print(battle(KNIGHTS))
