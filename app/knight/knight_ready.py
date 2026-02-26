from __future__ import annotations

from app.knight.knight import Knight


class KnightReady:
    def __init__(
            self,
            name: str,
            hp: int,
            protection: int,
            power: int
    ) -> None:
        self.name = name
        self.hp = hp
        self.protection = protection
        self.power = power

    @classmethod
    def prepare_knight(cls, knight: Knight) -> KnightReady:
        protection = 0
        if knight.armour:
            protection = sum([item.protection for item in knight.armour])
        power = knight.power + knight.weapon.power
        hp = knight.hp
        if knight.potion:
            power += knight.potion.effect.power
            hp += knight.potion.effect.hp
            protection += knight.potion.effect.protection
        return cls(
            name=knight.name,
            hp=hp,
            protection=protection,
            power=power
        )

    def fight(self, enemy: KnightReady) -> None:
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection
        if self.hp < 0:
            self.hp = 0
        if enemy.hp < 0:
            enemy.hp = 0
