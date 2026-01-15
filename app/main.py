from app.knights.class_knights import Knights
from app.knights.class_knights import battle_between


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


def from_dict(data: dict) -> Knights:

    return Knights(
        name=data["name"],
        power=data["power"],
        hp=data["hp"],
        armour=data.get("armour", []),
        weapon=data["weapon"],
        potion=data.get("potion")
    )


# BATTLE:
def battle(data: dict) -> dict:
    heroes = {key: from_dict(data) for key, data in data.items()}

    battle_between(heroes["lancelot"], heroes["mordred"])
    battle_between(heroes["arthur"], heroes["red_knight"])

    return {
        "Lancelot": heroes["lancelot"].hp,
        "Arthur": heroes["arthur"].hp,
        "Mordred": heroes["mordred"].hp,
        "Red Knight": heroes["red_knight"].hp,
    }


print(battle(KNIGHTS))
