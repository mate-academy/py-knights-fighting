from __future__ import annotations

from app.inventory.armour import Armour
from app.inventory.potion import Potion
from app.inventory.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            armours: list[Armour],
            potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armours = armours
        self.potion = potion

    def get_hp(self) -> int:
        return self.hp + self.potion.effect.hp

    def get_power(self) -> int:
        return self.power + self.weapon.power + self.potion.effect.power

    def get_protection(self) -> int:
        return (sum(armour.protection for armour in self.armours)
                + self.potion.effect.protection)

    def fight(self, other: Knight) -> dict[str, int]:
        damage_to_self = max(other.get_power() - self.get_protection(), 0)
        damage_to_other = max(self.get_power() - other.get_protection(), 0)

        self.hp = max(self.get_hp() - damage_to_self, 0)
        other.hp = max(other.get_hp() - damage_to_other, 0)

        return {
            self.name: self.hp,
            other.name: other.hp
        }
