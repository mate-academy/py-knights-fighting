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


def prepare_knight_for_battle(knight_data: dict) -> dict:
    knight_name = knight_data["name"]
    knight_hp = knight_data["hp"]
    knight_power = knight_data["power"] + knight_data["weapon"]["power"]

    knight_protection = sum(
        part["protection"] for part in knight_data["armour"]
    )

    if knight_data["potion"] is not None:
        effect = knight_data["potion"]["effect"]
        knight_hp += effect.get("hp", 0)
        knight_power += effect.get("power", 0)
        knight_protection += effect.get("protection", 0)

    return {
        "name": knight_name,
        "hp": knight_hp,
        "power": knight_power,
        "protection": knight_protection
    }


def knight_battle(knight_first: dict, knight_second: dict) -> dict:
    damage_to_knight_first = max(
        0, knight_second["power"] - knight_first["protection"]
    )
    damage_to_knight_second = max(
        0, knight_first["power"] - knight_second["protection"]
    )

    knight_first["hp"] -= damage_to_knight_first
    knight_second["hp"] -= damage_to_knight_second

    knight_first["hp"] = max(0, knight_first["hp"])
    knight_second["hp"] = max(0, knight_second["hp"])

    return {
        knight_first["name"]: knight_first["hp"],
        knight_second["name"]: knight_second["hp"]
    }


def battle(knightsconfig: dict) -> dict:
    lancelot = prepare_knight_for_battle(knightsconfig["lancelot"])
    mordred = prepare_knight_for_battle(knightsconfig["mordred"])
    arthur = prepare_knight_for_battle(knightsconfig["arthur"])
    red_knight = prepare_knight_for_battle(knightsconfig["red_knight"])

    result1 = knight_battle(lancelot, mordred)
    result2 = knight_battle(arthur, red_knight)

    return {**result1, **result2}
