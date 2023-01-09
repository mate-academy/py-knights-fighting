from knight import Knight


def battle_preparation(participants: dict):
    lancelot = Knight("lancelot", participants)
    arthur = Knight("arthur", participants)
    mordred = Knight("mordred", participants)
    red_knight = Knight("red_knight", participants)

    print(f"protection: {lancelot.protection}")
    print(f"power: {lancelot.power}")
    print(f"hp: {lancelot.hp}")
    lancelot.get_armour(participants["lancelot"]["armour"])
    lancelot.get_weapon(participants["lancelot"]["weapon"])
    lancelot.get_potion(KNIGHTS["lancelot"]["potion"])
    print("---------------")
    print(f"protection: {lancelot.protection}")
    print(f"power: {lancelot.power}")
    print(f"hp: {lancelot.hp}")
    mordred.get_armour(KNIGHTS["mordred"]["armour"])
    mordred.get_weapon(KNIGHTS["mordred"]["weapon"])
    mordred.get_potion(KNIGHTS["mordred"]["potion"])


# 1 Lancelot vs Mordred:
# 2 Arthur vs Red Knight:
# Return battle results:
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
battle_preparation(KNIGHTS)
