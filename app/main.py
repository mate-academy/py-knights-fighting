from app.knight_battle import KnightBattle


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


def battle(knights_config: dict) -> dict:
    knights_names = [key for key in knights_config]
    knights_instances = [
        KnightBattle(
            name=knights_config[knights_names[i]]["name"],
            power=knights_config[knights_names[i]]["power"],
            hp=knights_config[knights_names[i]]["hp"]
        ) for i in range(len(knights_config))
    ]

    for i, knight in enumerate(knights_instances):
        knight.knights_protection(knights_config[knights_names[i]]["armour"])
        knight.knights_power(knights_config[knights_names[i]]["weapon"])
        knight.potion_effects(knights_config[knights_names[i]]["potion"])

    for i in range(2, len(knights_instances)):
        knights_instances[i].battle(knights_instances[i - 2])

    result_hp = {}
    for knight in knights_instances:
        result_hp[knight.name] = knight.hp

    return result_hp
