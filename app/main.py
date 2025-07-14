from app.knights.knights import Knight

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


knight_instances = {}


def create_knights(knights: dict) -> None:
    for key in knights:
        knight_instances[key] = Knight(
            knights[key]["name"],
            knights[key]["power"],
            knights[key]["hp"]
        )


def apply_kit(knights: dict, knight_list: list) -> None:
    name_to_key = {knights[key]["name"]: key for key in knights}

    for knight in knight_list:
        key = name_to_key[knight.name]
        knight.apply_weapon(knights[key]["weapon"])
        knight.apply_armour(knights[key]["armour"])
        knight.apply_potion(knights[key]["potion"])


def results(knights: dict) -> dict:
    results = {}
    for knight in knights.values():
        results[knight.name] = knight.hp
    return results


def battle(knights_config: dict) -> dict:
    create_knights(knights_config)
    apply_kit(knights_config, Knight.knights)
    Knight.battle(knight_instances["lancelot"], knight_instances["mordred"])
    Knight.battle(knight_instances["arthur"], knight_instances["red_knight"])
    return results(knight_instances)


print(battle(KNIGHTS))
