from __future__ import annotations


class Knight:
    potions = []
    armours = []

    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def total_protection(self) -> int:
        protection = 0
        for armour in self.armours:
            protection += armour.protection

        if self.potions and "protection" in self.potions.effect:
            protection += self.potions.effect["protection"]

        return protection

    def total_power(self) -> int:
        power = self.power
        if hasattr(self, "weapon"):
            power += self.weapon.power
        if self.potions and "power" in self.potions.effect:
            power += self.potions.effect["power"]

        return power

    def total_hp(self) -> int:
        hp = self.hp
        if self.potions and "hp" in self.potions.effect:
            hp += self.potions.effect["hp"]

        return hp
