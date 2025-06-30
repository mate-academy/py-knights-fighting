from typing import Dict


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


def apply_armour(knight: Dict) -> int:
    return sum(a["protection"] for a in knight.get("armour", []))


def apply_potion_effects(knight: Dict) -> None:
    potion = knight.get("potion")
    if potion is None:
        return
    effects = potion.get("effect", {})
    knight["hp"] += effects.get("hp", 0)
    knight["power"] += effects.get("power", 0)
    knight["protection"] += effects.get("protection", 0)


def prepare_knight(knight: Dict) -> None:
    knight["protection"] = apply_armour(knight)
    knight["power"] += knight["weapon"]["power"]
    apply_potion_effects(knight)
    knight["hp"] = max(knight["hp"], 0)
    knight["power"] = max(knight["power"], 0)
    knight["protection"] = max(knight["protection"], 0)


def battle(knights_config: Dict) -> Dict[str, int]:
    for key in knights_config:
        prepare_knight(knights_config[key])

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    lancelot["hp"] = max(lancelot["hp"], 0)
    mordred["hp"] = max(mordred["hp"], 0)

    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    arthur["hp"] = max(arthur["hp"], 0)
    red_knight["hp"] = max(red_knight["hp"], 0)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
