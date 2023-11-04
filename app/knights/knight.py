from __future__ import annotations


class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

    def all_hp(self, hp_in_potion: int) -> int:
        self.hp += hp_in_potion
        return self.hp

    def all_power(self, power_in_weapon: int, power_in_potion: int) -> int:
        self.power += power_in_weapon + power_in_potion
        return self.power

    def all_protection(
            self,
            protection_in_armour: int,
            protection_in_potion: int
    ) -> int:
        self.protection += protection_in_armour + protection_in_potion
        return self.protection

    # not sure, if possible
    def __sub__(self, other: Knight) -> int:
        self.hp = self.hp - (other.power - self.protection)
        if self.hp < 0:
            self.hp = 0
        return self.hp
