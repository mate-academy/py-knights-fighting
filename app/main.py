from __future__ import annotations
from typing import Optional, List


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



class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: List[dict], weapon: dict, potion: Optional[dict] = None):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self):
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion:
            effects = self.potion.get("effect", {})
            for effect_type, effect_value in effects.items():
                setattr(self, effect_type, getattr(self, effect_type, 0) + effect_value)

def create_knight(data: dict) -> Knight:
    return Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"],
        armour=data["armour"],
        weapon=data["weapon"],
        potion=data.get("potion")
    )

def battle(knightsConfig):
    # Створення лицарів
    lancelot = create_knight(knightsConfig["lancelot"])
    arthur = create_knight(knightsConfig["arthur"])
    mordred = create_knight(knightsConfig["mordred"])
    red_knight = create_knight(knightsConfig["red_knight"])

    # Бій
    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # Перевірка, чи когось вбито в бою
    lancelot.hp = max(0, lancelot.hp)
    mordred.hp = max(0, mordred.hp)

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # Перевірка, чи когось вбито в бою
    arthur.hp = max(0, arthur.hp)
    red_knight.hp = max(0, red_knight.hp)

    # Повернення результатів бою
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
