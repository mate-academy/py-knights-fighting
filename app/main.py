from app.battle import fight


def apply_potion(knight: dict) -> None:
    """Applies potion effects to the knight if a potion is present."""
    potion = knight.get("potion")
    if potion and "effect" in potion:
        effect = potion["effect"]
        knight["power"] += effect.get("power", 0)
        knight["hp"] += effect.get("hp", 0)
        if "protection" in effect:
            knight["armour"].append(
                {"part": "potion", "protection": effect["protection"]})


def battle(knights: dict) -> dict:
    # Apply potions to all knights before the battles
    for knight in knights.values():
        apply_potion(knight)

    # Lancelot vs Mordred
    fight(knights["lancelot"], knights["mordred"])

    # Arthur vs Red Knight
    fight(knights["arthur"], knights["red_knight"])

    # Return battle results
    return {
        knights["lancelot"]["name"]: knights["lancelot"]["hp"],
        knights["arthur"]["name"]: knights["arthur"]["hp"],
        knights["mordred"]["name"]: knights["mordred"]["hp"],
        knights["red_knight"]["name"]: knights["red_knight"]["hp"],
    }


if __name__ == "__main__":
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
            "armour": [
                {"part": "breastplate", "protection": 15},
                {"part": "boots", "protection": 10},
            ],
            "weapon": {"name": "Poisoned Sword", "power": 60},
            "potion": {
                "name": "Berserk",
                "effect": {"power": +15, "hp": -5, "protection": +10},
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

    results = battle(KNIGHTS)
    print(results)
