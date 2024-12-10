from typing import Dict, Any

KNIGHTS: Dict[str, Dict[str, Any]] = {
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


def apply_armour(knight: Dict[str, Any]) -> None:
    knight["protection"] = sum(a["protection"] for a in knight["armour"])


def apply_weapon(knight: Dict[str, Any]) -> None:
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: Dict[str, Any]) -> None:
    if knight["potion"] is not None:
        for effect, value in knight["potion"]["effect"].items():
            if effect in knight:
                knight[effect] += value


def prepare_knight(knight: Dict[str, Any]) -> None:
    apply_armour(knight)
    apply_weapon(knight)
    apply_potion(knight)


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    # Підготовка лицарів
    for knight_key in knights_config:
        prepare_knight(knights_config[knight_key])

    # Битва: Lancelot vs Mordred
    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    lancelot["hp"] -= max(0, mordred["power"] - lancelot["protection"])
    mordred["hp"] -= max(0, lancelot["power"] - mordred["protection"])

    # Перевірка смертей
    lancelot["hp"] = max(0, lancelot["hp"])
    mordred["hp"] = max(0, mordred["hp"])

    # Битва: Arthur vs Red Knight
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]
    arthur["hp"] -= max(0, red_knight["power"] - arthur["protection"])
    red_knight["hp"] -= max(0, arthur["power"] - red_knight["protection"])

    # Перевірка смертей
    arthur["hp"] = max(0, arthur["hp"])
    red_knight["hp"] = max(0, red_knight["hp"])

    # Результат битви
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
