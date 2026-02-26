from __future__ import annotations

from app.knight.armour import Armour
from app.knight.potion.potion import Potion
from app.knight.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @classmethod
    def get_from_dict(cls, knight_dict : dict) -> Knight:
        return cls(
            name=knight_dict.get("name"),
            power=knight_dict.get("power"),
            hp=knight_dict.get("hp"),
            armour=[Armour.get_from_dict(item)
                    for item in knight_dict.get("armour")],
            weapon=Weapon.get_from_dict(knight_dict.get("weapon")),
            potion=Potion.get_from_dict(knight_dict.get("potion"))
            if knight_dict.get("potion") is not None
            else None
        )
