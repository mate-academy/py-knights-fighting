from copy import deepcopy


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
    knight["protection"] = sum(
        armour_part["protection"] for armour_part in knight["armour"]
    )


def apply_weapon(knight: dict) -> None:
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"] is None:
        return

    effect = knight["potion"]["effect"]
    knight["hp"] += effect.get("hp", 0)
    knight["power"] += effect.get("power", 0)
    knight["protection"] += effect.get("protection", 0)


def prepare_knight(knight: dict) -> None:
    apply_armour(knight)
    apply_weapon(knight)
    apply_potion(knight)


def fight(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    first_knight["hp"] = max(first_knight["hp"], 0)
    second_knight["hp"] = max(second_knight["hp"], 0)


def battle(knights_config: dict) -> dict:
    knights = deepcopy(knights_config)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    for knight in knights.values():
        prepare_knight(knight)

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
