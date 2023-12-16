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


def apply_equipment(knight: None) -> None:
    knight["protection"] = sum(a["protection"] for a in knight["armour"])

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        effects = knight["potion"]["effect"]
        for key, value in effects.items():
            knight[key] += value


def perform_battle(knight1: None, knight2: None) -> None:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    # check if someone fell in battle
    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knights_config: None) -> dict:

    for knight in knights_config.values():
        apply_equipment(knight)

    battle_pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for knight1_name, knight2_name in battle_pairs:
        knight1 = knights_config[knight1_name]
        knight2 = knights_config[knight2_name]
        perform_battle(knight1, knight2)

    return {knight["name"]: knight["hp"] for knight in knights_config.values()}


print(battle(KNIGHTS))
