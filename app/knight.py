from __future__ import annotations

from app.inventory.armor import Armor
from app.inventory.potion import Potion
from app.inventory.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armor: list[Armor],
            weapon: Weapon,
            potion: Potion,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        self.apply_armor(armor)
        self.apply_weapon(weapon)
        self.apply_potion(potion)

    def apply_armor(self, armor: list[Armor]) -> None:
        for item in armor:
            self.protection += item.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Potion | None) -> None:
        if potion is not None:
            if potion.effect.power:
                self.power += potion.effect.power
            if potion.effect.hp:
                self.hp += potion.effect.hp
            if potion.effect.protection:
                self.protection += potion.effect.protection

    def attack(self, enemy: Knight) -> None:
        enemy.get_hit(self.power)

    def get_hit(self, attack_power: int) -> None:
        protected_damage = attack_power - self.protection
        if self.hp >= protected_damage:
            self.hp -= protected_damage
        else:
            self.hp = 0
