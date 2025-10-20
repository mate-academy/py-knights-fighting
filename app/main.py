# Original KNIGHTS data, as expected by the tests. Do not change this.
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
            "effect": {"hp": -5, "power": +15, "protection": +10},
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


def _duel(knight1_stats: dict, knight2_stats: dict) -> tuple[int, int]:
    """Calculates the result of a single duel, returning final HP for both."""
    damage_to_knight1 = max(0, knight2_stats["power"] - knight1_stats["protection"])
    hp1_after_battle = knight1_stats["hp"] - damage_to_knight1

    damage_to_knight2 = max(0, knight1_stats["power"] - knight2_stats["protection"])
    hp2_after_battle = knight2_stats["hp"] - damage_to_knight2

    return max(0, hp1_after_battle), max(0, hp2_after_battle)


def battle(knights_config: dict) -> dict:
    """
    Conducts two fixed battles (Lancelot vs Mordred, Arthur vs Red Knight)
    and returns the final HP of all knights.
    """
    lancelot = _prepare_knight_stats(knights_config["lancelot"])
    mordred = _prepare_knight_stats(knights_config["mordred"])
    arthur = _prepare_knight_stats(knights_config["arthur"])
    red_knight = _prepare_knight_stats(knights_config["red_knight"])

    lancelot_hp, mordred_hp = _duel(lancelot, mordred)
    arthur_hp, red_knight_hp = _duel(arthur, red_knight)

    return {
        knights_config["lancelot"]["name"]: lancelot_hp,
        knights_config["mordred"]["name"]: mordred_hp,
        knights_config["arthur"]["name"]: arthur_hp,
        knights_config["red_knight"]["name"]: red_knight_hp,
    }
