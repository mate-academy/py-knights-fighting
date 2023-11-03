from __future__ import annotations


class Knight:
    potion = None
    armours = []
    protection = 0

    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def total_protection(self) -> int:
        protection = 0
        for armour in self.armours:
            protection += armour.protection

        if self.potion and self.potion.protection:
            protection += self.potion.protection

        return protection

    def total_power(self) -> int:
        power = self.power
        if hasattr(self, "weapon"):
            power += self.weapon.power
        if self.potion and self.potion.power:
            power += self.potion.power

        return power

    def total_hp(self) -> int:
        hp = self.hp
        if self.potion and self.potion.hp:
            hp += self.potion.hp

        return hp
