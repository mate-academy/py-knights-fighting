from typing import Dict
from app.entities.knight import Knight, Armour, Weapon, Potion
from app.battle.battle import Battle


def battle(knights_config: Dict[str, Dict]) -> Dict[str, Battle]:
    knights = {
        name: Knight(
            config["name"],
            config["power"],
            config["hp"],
            [Armour(a["part"], a["protection"]) for a in config["armour"]],
            Weapon(config["weapon"]["name"], config["weapon"]["power"]),
            Potion(
                config["potion"]["name"], config["potion"]["effect"]
            ) if config["potion"] else None
        ) for name, config in knights_config.items()
    }
    battle_pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
    battle = Battle(knights)
    return battle.start(battle_pairs)


def main(knights_config: Dict[str, Dict]) -> None:
    print(battle(knights_config))


if __name__ == "__main__":
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

    main(KNIGHTS)
