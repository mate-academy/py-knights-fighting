"""
Each squire helps his lord,
carries his weapons, armor and potion until the battle begins
"""

from typing import Any
from app.human.knight import Knight


class Squire:
    def __init__(self,
                 armor_list: list[dict[str: Any]],
                 weapon: dict[str: Any]) -> Any:
        self.armor_list = armor_list
        self.weapon = weapon
        self.potion = None
        self.my_lord: "Knight" = None

    def set_my_lord(self, my_lord: Knight) -> None:
        self.my_lord = my_lord

