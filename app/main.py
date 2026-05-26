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
    """Applies armour, weapon and potion effects to a knight."""
    result = knight.copy()

    # armour
    result["protection"] = sum(
        piece["protection"]
        for piece in result["armour"]
    )

    # weapon
    result["power"] += result["weapon"]["power"]

    # potion
    potion = result.get("potion")
    if potion:
        effect = potion["effect"]
        result["hp"] += effect.get("hp", 0)
        result["power"] += effect.get("power", 0)
        result["protection"] += effect.get("protection", 0)

    return result


def fight(attacker: dict, defender: dict) -> None:
    """Simulates one fight exchange between two knights."""

    attacker_damage = max(0, defender["power"] - attacker["protection"])
    defender_damage = max(0, attacker["power"] - defender["protection"])

    attacker["hp"] -= attacker_damage
    defender["hp"] -= defender_damage

    attacker["hp"] = max(0, attacker["hp"])
    defender["hp"] = max(0, defender["hp"])


def battle(knights_config: dict) -> dict:
    # prepare all knights
    knights = {
        name: prepare_knight(knight)
        for name, knight in knights_config.items()
    }

    # battles
    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for attacker_name, defender_name in battles:
        fight(knights[attacker_name], knights[defender_name])

    # result
    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }


print(battle(KNIGHTS))
