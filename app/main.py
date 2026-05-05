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
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
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
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
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
            },
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {"part": "breastplate", "protection": 25},
        ],
        "weapon": {
            "name": "Sword",
            "power": 45,
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def get_knight_stats(knight: dict) -> dict:
    stats = {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"] + knight["weapon"]["power"],
        "protection": sum(
            part["protection"] for part in knight["armour"]
        ),
    }

    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            stats[stat] += value

    return stats


def fight(first: dict, second: dict) -> None:
    first["hp"] -= second["power"] - first["protection"]
    second["hp"] -= first["power"] - second["protection"]

    first["hp"] = max(first["hp"], 0)
    second["hp"] = max(second["hp"], 0)


def battle(knights_config: dict) -> dict:
    lancelot = get_knight_stats(knights_config["lancelot"])
    arthur = get_knight_stats(knights_config["arthur"])
    mordred = get_knight_stats(knights_config["mordred"])
    red_knight = get_knight_stats(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
