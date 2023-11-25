from typing import Optional, List, Dict, Union


class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armour: List[Dict[str, Union[str, int]]],
                 weapon: Dict[str, Union[str, int]],
                 potion: Optional[Dict[str, Union[str, Dict[str, int]]]]
                 = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()

    def apply_armor(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)
        return self

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]
        return self

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            for stat, value in effect.items():

                if stat == "hp":
                    self.hp += value
                elif stat == "power":
                    self.power += value
                elif stat == "protection":
                    self.protection += value
        return self


knights_config = {
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
