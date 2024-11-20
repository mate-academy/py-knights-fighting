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
                Potion.empty()
                if value.get("potion") is None
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
