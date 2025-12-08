from app.knight import Knight

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


def prepare_knight(config: dict) -> Knight:
    knight = Knight(config)
    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()
    return knight


def battle(knights_config: dict) -> dict:
    prepared = {k: prepare_knight(v) for k, v in knights_config.items()}
    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for first_knight, second_knight in pairs:
        fk = prepared[first_knight]
        sk = prepared[second_knight]
        dmg_to_fk = max(0, sk.power - fk.protection)
        fk.hp = max(0, fk.hp - dmg_to_fk)
        dmg_to_sk = max(0, fk.power - sk.protection)
        sk.hp = max(0, sk.hp - dmg_to_sk)
    result_knights = [prepared["lancelot"], prepared["arthur"],
                      prepared["mordred"], prepared["red_knight"]]
    return {k.name: k.hp for k in result_knights}
