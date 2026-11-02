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


def prepare_knight(knight: dict) -> dict:
    # sum of all armour parts (0 if the list is empty)
    protection = sum(part["protection"] for part in knight["armour"])
    power = knight["power"] + knight["weapon"]["power"]
    hp = knight["hp"]

    if knight["potion"] is not None:
        effect = knight["potion"]["effect"]
        power += effect.get("power", 0)
        protection += effect.get("protection", 0)
        hp += effect.get("hp", 0)

    # a NEW dict: the original config is not modified
    return {
        "name": knight["name"],
        "hp": hp,
        "power": power,
        "protection": protection,
    }


def duel(first: dict, second: dict) -> None:
    first["hp"] -= second["power"] - first["protection"]
    second["hp"] -= first["power"] - second["protection"]
    first["hp"] = max(first["hp"], 0)
    second["hp"] = max(second["hp"], 0)


def battle(knights_config: dict) -> dict:
    knights = {
        key: prepare_knight(config)
        for key, config in knights_config.items()
    }

    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    return {knight["name"]: knight["hp"] for knight in knights.values()}
