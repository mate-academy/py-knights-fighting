from typing import Union

from app.outfit.armour import Armour
from app.outfit.potion.effect import Effect
from app.outfit.potion.potion import Potion
from app.outfit.weapon import Weapon


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: Union[list[dict], list],
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [
            Armour(**armour)
            for armour in armour
        ] if armour else []
        self.weapon = Weapon(**weapon)
        self.potion = Potion(
            potion["name"], Effect(**potion["effect"])
        ) if potion else None
        self.protection = 0

    def apply_armour(self) -> None:
        if self.armour:
            for item in self.armour:
                self.protection += item.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.power += self.potion.effect.power
            self.protection += self.potion.effect.protection
            self.hp += self.potion.effect.hp

    def battle_preparation(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def fell_in_battle(self) -> None:
        if self.hp < 0:
            self.hp = 0
