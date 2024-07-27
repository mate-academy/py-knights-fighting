from app.human.knight import Knight

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


def battle(knights_config: dict) -> None:
    knights = {}
    for name, config in knights_config.items():
        knight = Knight(config["name"], config["power"], config["hp"])
        knight.prepare_for_battle(knights_config)
        knights[knight.name] = knight

    fight_pairs = [
        ("Lancelot", "Mordred"),
        ("Arthur", "Red Knight")
    ]

    results = {}

    for knight1_name, knight2_name in fight_pairs:
        knight1 = knights[knight1_name]
        knight2 = knights[knight2_name]

        knight1.hp -= knight2.power - knight1.armor
        knight2.hp -= knight1.power - knight2.armor

        if knight1.hp <= 0:
            knight1.hp = 0
        if knight2.hp <= 0:
            knight2.hp = 0

        results[knight1.name] = knight1.hp
        results[knight2.name] = knight2.hp

    return results
