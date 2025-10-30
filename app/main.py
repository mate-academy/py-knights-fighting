from knights import Knight

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
    knights = []
    for identify in knights_config:
        info = knights_config[identify]
        knight_obj = Knight(
            name=info["name"],
            power=info["power"],
            hp=info["hp"],
            weapon=info["weapon"],
            armour=info["armour"],
            potion=info["potion"]
        )
        knights.append(knight_obj)

    battles = [
        (knights[0], knights[2]),
        (knights[1], knights[3])
    ]

    def fight(knight1: Knight, knight2: Knight) -> None:
        knight2.hp -= max(0, knight1.power - knight2.total_protection)
        knight1.hp -= max(0, knight2.power - knight1.total_protection)
        knight1.hp = max(0, knight1.hp)
        knight2.hp = max(0, knight2.hp)

    for k1, k2 in battles:
        fight(k1, k2)

    return {k.name: k.hp for k in knights}


print(battle(KNIGHTS))
