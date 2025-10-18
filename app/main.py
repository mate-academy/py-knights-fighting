# Повністю замініть вміст app/main.py на цей код

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [
            {
                "name": "Metal Sword",
                "power": 50,
            }
        ],
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
            },
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Magic Staff", "power": 60},
        "potion": {
            "name": "Poison",
            "effect": {
                "hp": -10,
                "power": +15,
            },
        },
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
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def _prepare_knight_stats(knight_data: dict) -> dict:
    """Calculates final stats for a single knight."""
    protection = 0
    # Note: Lancelot's armour data is structured differently in the source.
    # This check handles both cases.
    if knight_data["armour"] and "protection" in knight_data["armour"][0]:
        for armour_part in knight_data["armour"]:
            protection += armour_part.get("protection", 0)

    power = knight_data["power"]
    if knight_data.get("weapon"):
        power += knight_data["weapon"]["power"]
    # Handle Lancelot's sword which is in the "armour" list
    elif knight_data["armour"] and "power" in knight_data["armour"][0]:
        power += knight_data["armour"][0].get("power", 0)

    hp = knight_data["hp"]

    if knight_data["potion"]:
        effect = knight_data["potion"]["effect"]
        hp += effect.get("hp", 0)
        power += effect.get("power", 0)
        protection += effect.get("protection", 0)

    return {"hp": hp, "power": power, "protection": protection}


def battle(knights_config: dict) -> dict:
    """
    Conducts battles between knights and returns the result.
    """
    # Prepare stats for all knights
    lancelot = _prepare_knight_stats(knights_config["lancelot"])
    mordred = _prepare_knight_stats(knights_config["mordred"])
    arthur = _prepare_knight_stats(knights_config["arthur"])
    red_knight = _prepare_knight_stats(knights_config["red_knight"])

    # Battle 1: Lancelot vs Mordred
    lancelot_hp = lancelot["hp"] - (mordred["power"] - lancelot["protection"])
    mordred_hp = mordred["hp"] - (lancelot["power"] - mordred["protection"])

    # Battle 2: Arthur vs Red Knight
    arthur_hp = arthur["hp"] - (red_knight["power"] - arthur["protection"])
    red_knight_hp = red_knight["hp"] - (arthur["power"] - red_knight["protection"])

    # Format the final result, ensuring HP is not negative
    return {
        "Lancelot": max(0, lancelot_hp),
        "Mordred": max(0, mordred_hp),
        "Arthur": max(0, arthur_hp),
        "Red Knight": max(0, red_knight_hp),
    }