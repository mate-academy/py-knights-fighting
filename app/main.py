KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50},
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
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [{"part": "leather_vest", "protection": 10}],
        "weapon": {"name": "Magic Staff", "power": 60},
        "potion": {
            "name": "Poison",
            "effect": {"hp": -10, "power": +15},
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {"hp": +10, "power": +5},
        },
    },
}


def _prepare_knight_stats(knight_data: dict) -> dict:
    """Calculates final stats for a single knight based on their equipment."""
    protection = sum(
        part.get("protection", 0) for part in knight_data.get("armour", [])
    )
    power = knight_data["power"] + knight_data["weapon"]["power"]
    hp = knight_data["hp"]

    if knight_data.get("potion"):
        effect = knight_data["potion"].get("effect", {})
        hp += effect.get("hp", 0)
        power += effect.get("power", 0)
        protection += effect.get("protection", 0)

    return {"hp": hp, "power": power, "protection": protection}


def battle(knights_config: dict) -> dict:
    """Conducts battles and returns the final HP of all knights."""
    lancelot = _prepare_knight_stats(knights_config["lancelot"])
    mordred = _prepare_knight_stats(knights_config["mordred"])
    arthur = _prepare_knight_stats(knights_config["arthur"])
    red_knight = _prepare_knight_stats(knights_config["red_knight"])

    # Battle 1: Lancelot vs Mordred
    lancelot_hp = lancelot["hp"] - max(0, mordred["power"] - lancelot["protection"])
    mordred_hp = mordred["hp"] - max(0, lancelot["power"] - mordred["protection"])

    # Battle 2: Arthur vs Red Knight
    arthur_hp = arthur["hp"] - max(0, red_knight["power"] - arthur["protection"])
    red_knight_hp = red_knight["hp"] - max(0, arthur["power"] - red_knight["protection"])

    # Use actual names from config for the result keys
    return {
        knights_config["lancelot"]["name"]: max(0, lancelot_hp),
        knights_config["mordred"]["name"]: max(0, mordred_hp),
        knights_config["arthur"]["name"]: max(0, arthur_hp),
        knights_config["red_knight"]["name"]: max(0, red_knight_hp),
    }
