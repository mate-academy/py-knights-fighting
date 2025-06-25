from app.knights import Knight


knights_dict = {
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


def battle(knights_dict: dict) -> dict:
    lancelot = Knight(**knights_dict["lancelot"])
    mordred = Knight(**knights_dict["mordred"])
    arthur = Knight(**knights_dict["arthur"])
    red_knight = Knight(**knights_dict["red_knight"])

    for knight in (lancelot, mordred, arthur, red_knight):
        knight.add_protection()
        knight.add_power()
        knight.add_hp()

    lancelot.hp -= mordred.power - lancelot.total_protection
    mordred.hp -= lancelot.power - mordred.total_protection
    lancelot.hp = max(lancelot.hp, 0)
    mordred.hp = max(mordred.hp, 0)

    arthur.hp -= red_knight.power - arthur.total_protection
    red_knight.hp -= arthur.power - red_knight.total_protection
    arthur.hp = max(arthur.hp, 0)
    red_knight.hp = max(red_knight.hp, 0)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knights_dict))
