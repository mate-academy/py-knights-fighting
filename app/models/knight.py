# app/models/knight.py

from app.models.armour import Armour
from app.models.potion import Potion
from app.models.weapon import Weapon


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        weapon: Weapon,
        armour: list[Armour] | None = None,
        potion: Potion | None = None,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.weapon = weapon
        self.armour = armour or []
        self.potion = potion

    @property
    def protection(self) -> int:
        value = sum(item.protection for item in self.armour)

        if self.potion:
            value += self.potion.effect.get("protection", 0)

        return value

    @property
    def battle_power(self) -> int:
        value = self.power + self.weapon.power

        if self.potion:
            value += self.potion.effect.get("power", 0)

        return value

    @property
    def battle_hp(self) -> int:
        value = self.hp

        if self.potion:
            value += self.potion.effect.get("hp", 0)

        return value
