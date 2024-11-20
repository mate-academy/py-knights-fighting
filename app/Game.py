from typing import Dict

from app.Equipment import Armour, Weapon, Potion
from app.Knight import Knight


class Game:
    def __init__(self, knights_data: dict) -> None:
        self.knights_data = knights_data

    @staticmethod
    def create_knights(knights_data: Dict) -> Dict[str, Knight]:
        knights = {}
        for key, value in knights_data.items():
            armour = Armour(value.get("armour"))
            weapon = Weapon(**value.get("weapon"))
            potion = (
                Potion.empty() if value.get("potion") is None
                else Potion(**value.get("potion"))
            )
            effects = potion.apply_effect(
                power=weapon.power,
                hp=value.get("hp"),
                protection=armour.sum_protection(),
            )
            knights[key] = Knight(
                name=value["name"],
                power=effects["power"] + value["power"],
                hp=effects["hp"],
                armour=effects["protection"],
                weapon=weapon.power,
                potion=potion,
            )
        return knights

    # @staticmethod
    # def battle(knight1: Knight, knight2: Knight) -> str:
    #
    #     damage_knight1 = knight1.power + knight1.weapon - knight2.armour
    #     damage_knight2 = knight2.power + knight2.weapon - knight1.armour
    #
    #     damage_knight1 = max(damage_knight1, 0)
    #     damage_knight2 = max(damage_knight2, 0)
    #
    #     while knight1.hp > 0 and knight2.hp > 0:
    #         knight1.hp -= damage_knight2
    #         knight2.hp -= damage_knight1
    #         if knight1.hp <= 0:
    #             return f"{knight2.name} победил!"
    #         if knight2.hp <= 0:
    #             return f"{knight1.name} победил!"
    #
    #     return "Ничья"


if __name__ == "__main__":
    ex = knights_data = {
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
        }
    }
    game = Game(knights_data)
    knights = game.create_knights(knights_data)

    result = game.battle(knights["lancelot"], knights["arthur"])
    print(result)
