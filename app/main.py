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


def apply_armour(knight: dict) -> None:
    knight["protection"] = 0
    for arm in knight["armour"]:
        knight["protection"] += arm["protection"]


def apply_weapon(knight: dict) -> None:
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        for effect in knight["potion"]["effect"]:
            knight[effect] += knight["potion"]["effect"][effect]


def apply_battle_effects(knights_config: dict) -> None:
    for knight_name in knights_config:
        knight = knights_config[knight_name]
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)


def fight(attacker: dict, defender: dict) -> None:
    attacker["hp"] -= defender["power"] - attacker["protection"]
    defender["hp"] -= attacker["power"] - defender["protection"]

    if attacker["hp"] <= 0:
        attacker["hp"] = 0

    if defender["hp"] <= 0:
        defender["hp"] = 0


def battle(knights_config: dict) -> dict:
    apply_battle_effects(knights_config)

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    # Lancelot vs Mordred
    fight(lancelot, mordred)

    # Arthur vs Red Knight
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
