from typing import Dict, List, Optional, Union


class Knight:
    def __init__(self, config: Dict[str, Union[str, int, List[Dict[str, int]], Dict[str, Union[str, Dict[str, int]]]]]) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = 0

    def apply_armour(self):
        for a in self.armour:
            self.protection += a["protection"]

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion is not None:
            for stat, value in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def attack(self, opponent) -> None:
        opponent.hp -= max(self.power - opponent.protection, 0)
        opponent.hp = max(opponent.hp, 0)


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


def battle(knights_config):
    knights = {k: Knight(v) for k, v in knights_config.items()}
    for knight in knights.values():
        knight.prepare_for_battle()

        self.apply_potion()

    def attack(self, opponent):
        opponent.hp -= max(self.power - opponent.protection, 0)
        opponent.hp = max(opponent.hp, 0)


def battle(knights_config):
    knights = {k: Knight(v) for k, v in knights_config.items()}
    for knight in knights.values():
        knight.prepare_for_battle()

    knights["lancelot"].attack(knights["mordred"])
    knights["mordred"].attack(knights["lancelot"])

    knights["arthur"].attack(knights["red_knight"])
    knights["red_knight"].attack(knights["arthur"])

    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }

print(battle(KNIGHTS))
