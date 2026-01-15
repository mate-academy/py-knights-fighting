from app.battle_preparation.battle_pref import battle_pref

knights = {
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

    new_pref_knights = battle_pref(knights_config)

    knight_l = []
    for knight, kn_value in new_pref_knights.items():
        knight_l.append(kn_value)

    knight1 = knight_l[0]
    knight2 = knight_l[1]
    knight3 = knight_l[2]
    knight4 = knight_l[3]

    knight_range = [knight1, knight2, knight3, knight4]

    knight1["hp"] -= knight3["power"] - knight1["protection"]
    knight3["hp"] -= knight1["power"] - knight3["protection"]
    knight2["hp"] -= knight4["power"] - knight2["protection"]
    knight4["hp"] -= knight2["power"] - knight4["protection"]

    for knight in knight_range:
        if knight["hp"] <= 0:
            knight["hp"] = 0

    return {
        knight1["name"]: knight1["hp"],
        knight2["name"]: knight2["hp"],
        knight3["name"]: knight3["hp"],
        knight4["name"]: knight4["hp"],
    }
