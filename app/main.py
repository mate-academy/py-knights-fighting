from app.Knight import Knight


def battle(knights_config: dict) -> dict:
    for knight in knights_config:
        object_knight = Knight(
            knights_config[knight]["name"],
            knights_config[knight]["power"],
            knights_config[knight]["hp"],
            knights_config[knight]["armour"],
            knights_config[knight]["weapon"],
            knights_config[knight]["potion"]
        )

        knights_config[knight] = object_knight

        knights_config[knight].apply_armour()
        knights_config[knight].apply_weapon()
        if knights_config[knight].potion is not None:
            knights_config[knight].apply_potion()

    knights_config["lancelot"].battle(knights_config["mordred"])
    knights_config["arthur"].battle(knights_config["red_knight"])

    return {
        knight[1].name: knight[1].hp
        for knight in knights_config.items()
    }


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

print(battle(KNIGHTS))
