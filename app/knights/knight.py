from __future__ import annotations
from app.knights.weapon import Weapon
from app.knights.armour import Armour
from app.knights.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion | None = None,
    ) -> None:
        self.name = name

        self.base_hp = hp
        self.base_power = power

        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.hp = self.calculate_hp()
        self.power = self.calculate_power()
        self.protection = self.calculate_protection()

    def calculate_hp(self) -> int:
        hp = self.base_hp

        if self.potion:
            hp += self.potion.effect.get("hp", 0)

        return hp

    def calculate_power(self) -> int:
        power = self.base_power + self.weapon.power

        if self.potion:
            power += self.potion.effect.get("power", 0)

        return power

    def calculate_protection(self) -> int:
        protection = sum(
            piece.protection for piece in self.armour
        )

        if self.potion:
            protection += self.potion.effect.get(
                "protection",
                0,
            )

        return protection

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection

        if damage < 0:
            damage = 0

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0
