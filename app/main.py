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


def prepare_knight_stats(knight: dict) -> dict:
    knight["protection"] = sum(arm["protection"]
                               for arm in knight.get("armour", []))

    knight["power"] += knight["weapon"]["power"]

    potion = knight.get("potion")
    if potion:
        effect = potion.get("effect", {})
        knight["hp"] += effect.get("hp", 0)
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)

    return knight


def apply_damage(attacker: dict, defender: dict) -> None:
    damage = attacker["power"] - defender["protection"]
    defender["hp"] -= damage

    if defender["hp"] < 0:
        defender["hp"] = 0


def battle(knights_config: dict) -> dict:
    lancelot = prepare_knight_stats(knights_config["lancelot"])
    arthur = prepare_knight_stats(knights_config["arthur"])
    mordred = prepare_knight_stats(knights_config["mordred"])
    red_knight = prepare_knight_stats(knights_config["red_knight"])

    apply_damage(mordred, lancelot)
    apply_damage(lancelot, mordred)

    apply_damage(red_knight, arthur)
    apply_damage(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
