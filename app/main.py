from app.knight import Knight


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


def create_knight(config: dict) -> Knight:
    return Knight(
        name=config["name"],
        power=config["power"],
        hp=config["hp"],
        armour=config.get("armour", []),
        weapon=config["weapon"],
        potion=config.get("potion")
    )


def battle(knightsconfig: dict) -> dict:
    knights = {
        name: create_knight(info) for name, info in knightsconfig.items()
    }

    # Lancelot vs Mordred
    knights["lancelot"].receive_damage(knights["mordred"].power)
    knights["mordred"].receive_damage(knights["lancelot"].power)

    # Arthur vs Red Knight
    knights["arthur"].receive_damage(knights["red_knight"].power)
    knights["red_knight"].receive_damage(knights["arthur"].power)
    return {knight.name: knight.hp for knight in knights.values()}


results = battle(KNIGHTS)
print(results)
