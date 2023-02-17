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
        for buff, value in potion.effect.items():
            setattr(
                self,
                buff,
                getattr(self, buff) + value
            )

    def apply_armour(self, armour: list[Armour]) -> None:
        self.protection = sum(
            armour_element.protection for armour_element in armour
        )

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    @staticmethod
    def fight(
            first_knight: Knight,
            second_knight: Knight
    ) -> None:
        first_knight.take_damage(second_knight)
        second_knight.take_damage(first_knight)

    def check_health(self) -> int:
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def take_damage(self, enemy: Knight) -> None:
        if self.protection < enemy.power:
            self.hp -= enemy.power - self.protection

        self.check_health()
