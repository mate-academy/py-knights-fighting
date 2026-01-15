from __future__ import annotations
from typing import Optional

from app.items.weapon import Weapon
from app.items.armour import Armour
from app.items.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            weapon: dict | Weapon,
            armour: list[dict] | list[Armour],
            hp: int = 0,
            power: int = 0,
            protection: int = 0,
            potion: Optional[dict | Potion] = None
    ) -> None:
        self.name = name
        self.weapon = Weapon(**weapon) if isinstance(weapon, dict) else weapon
        self.armour = (
            [Armour(**part) for part in armour]
            if armour and isinstance(armour[0], dict)
            else armour
        )
        self.hp = hp
        self.power = power
        self.protection = protection
        self.potion = (
            Potion(**potion)
            if potion and isinstance(potion, dict)
            else potion
        )
        self.prepare_for_battle()

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, value)

    def equip_weapon(self) -> None:
        self.power += self.weapon.power

    def equip_armour(self) -> None:
        for part in self.armour:
            self.protection += part.protection

    def drink_potion(self) -> None:
        if not self.potion:
            return
        self.power += self.potion.power
        self.hp += self.potion.hp
        self.protection += self.potion.protection

    def prepare_for_battle(self) -> None:
        self.equip_weapon()
        self.equip_armour()
        self.drink_potion()
