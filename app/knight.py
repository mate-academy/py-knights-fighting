from typing import Dict
from app.config import KNIGHT


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict[str, str], dict[str, int]],
            weapon: dict[str, str],
            potion: dict[str, int],
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for i in self.armour:
            self.protection += i["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            for key, value in self.potion["effect"].items():
                if key == "power":
                    self.power += value
                elif key == "protection":
                    self.protection += value
                elif key == "hp":
                    self.hp += value


def create_knight(knight_dict: Dict) -> KNIGHT:
    return Knight(
        name=knight_dict["name"],
        power=knight_dict["power"],
        hp=knight_dict["hp"],
        armour=knight_dict["armour"],
        weapon=knight_dict["weapon"],
        potion=knight_dict["potion"]
    )
