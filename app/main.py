# Knights stats
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


def prepare_knight(knight: dict) -> None:
    # Battle preparations

    knight["protection"] = 0

    for i in knight["armour"]:
        knight["protection"] += i["protection"]

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if it exists
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]

    # -------------------------------------------------------------------------------


def fight(knight1: dict, knight2: dict) -> None:
    # Fight logic
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    # Check if someone fell in battle
    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0


def battle(knightsconfig: dict) -> dict:
    for knight in knightsconfig.values():
        prepare_knight(knight)

    # Get individual knights
    lancelot = knightsconfig["lancelot"]
    arthur = knightsconfig["arthur"]
    mordred = knightsconfig["mordred"]
    red_knight = knightsconfig["red_knight"]

    # Battle:

    # 1. Lancelot vs Mordred
    fight(lancelot, mordred)

    # 2. Arthur vs Red Knight
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
