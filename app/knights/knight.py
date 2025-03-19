from typing import Dict, Any
from app.knights.potion import Potion


# base function
class Knight:
    def __init__(self, name: str, data: Dict[str, Any]) -> None:
        self.name = name
        self.data = data
        self.power = 0
        self.hp = 0
        self.armour = 0
        self.weapon = None
        self.potion = None
        self.final_hp = 0
        self.final_armour = 0
        self.final_power = 0

    def calculate_stats(self) -> None:
        self.power = self.data["power"]
        self.hp = self.data["hp"]
        self.weapon = self.data["weapon"]

        if self.data["potion"]:
            self.potion = Potion(
                name=self.data["potion"]["name"],
                effect=self.data["potion"]["effect"]
            )
        else:
            self.potion = None

    # calculate armour sum from armour.py
    def calculate_armour(self) -> None:
        armour_sum = 0
        for armour_element in self.data["armour"]:
            armour_sum += armour_element["protection"]
        self.armour = armour_sum

    def final_stats(self) -> None:
        if self.potion:
            hp = self.hp + self.potion.extra_hp()  # fixed here
            power = (self.power + self.weapon["power"]
                     + self.potion.extra_power())
            armour = self.armour + self.potion.extra_protection()  # fixed here
        else:
            hp = self.hp
            power = self.power + self.weapon["power"]
            armour = self.armour

        self.final_hp = hp
        self.final_power = power
        self.final_armour = armour
