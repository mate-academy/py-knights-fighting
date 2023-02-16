from __future__ import annotations

from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            hp: int = 0,
            power: int = 0,
            armour: list[Armour] | None = None,
            weapon: Weapon | None = None,
            potion: Potion | None = None
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

        if armour is not None:
            self.apply_armour(armour)

        if weapon is not None:
            self.apply_weapon(weapon)

        if potion is not None:
            self.apply_potion(potion)

    def apply_potion(self, potion: Potion) -> None:
        if "power" in potion.effect:
            self.power += potion.effect["power"]

        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]

        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]

    def apply_armour(self, armour: list[Armour]) -> None:
        self.protection = sum(
            [armour_element.protection for armour_element in armour]
        )

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    @staticmethod
    def fight(
            fst_knight: Knight,
            snd_knight: Knight
    ) -> None:
        if fst_knight.protection < snd_knight.power:
            fst_knight.hp -= snd_knight.power - fst_knight.protection

        if snd_knight.protection < fst_knight.power:
            snd_knight.hp -= fst_knight.power - snd_knight.protection

        if fst_knight.hp < 0:
            fst_knight.hp = 0

        if snd_knight.hp < 0:
            snd_knight.hp = 0
