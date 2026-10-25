from app.utils import prepare


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


def battle(knightsconfig: dict) -> dict:
    # BATTLE PREPARATIONS:
    prepare(knightsconfig["lancelot"])
    prepare(knightsconfig["mordred"])
    prepare(knightsconfig["red_knight"])
    prepare(knightsconfig["arthur"])

    lancelot = knightsconfig["lancelot"]
    mordred = knightsconfig["mordred"]
    red_knight = knightsconfig["red_knight"]
    arthur = knightsconfig["arthur"]

    if (lancelot["power"] - mordred["protection"]) > 0:
        mordred["hp"] = (mordred["hp"]
                         - (lancelot["power"] - mordred["protection"]))
    if (mordred["power"] - lancelot["protection"]) > 0:
        lancelot["hp"] = (lancelot["hp"]
                          - (mordred["power"] - lancelot["protection"]))

    if (red_knight["power"] - arthur["protection"]) > 0:
        arthur["hp"] = (arthur["hp"]
                        - (red_knight["power"] - arthur["protection"]))
    if (arthur["power"] - red_knight["protection"]) > 0:
        red_knight["hp"] = (red_knight["hp"]
                            - (arthur["power"] - red_knight["protection"]))

    for knight in knightsconfig.values():
        if knight["hp"] <= 0:
            knight["hp"] = 0

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
