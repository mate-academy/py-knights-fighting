from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = self.calculate_protection()

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion["effect"].items():
                if hasattr(self, stat):
                    setattr(self, stat, getattr(self, stat) + value)

    def calculate_protection(self) -> int:
        protection = sum(armour["protection"] for armour in self.armour)
        return protection

    def attack(
            self,
            opponent: Knight
    ) -> int:
        damage = self.power - opponent.protection
        return damage

    def take_damage(
            self,
            damage: int
    ) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
