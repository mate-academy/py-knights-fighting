from __future__ import annotations

from app.knights_fighting.boosts import Potion
from app.knights_fighting.equipment import Armour, Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        self.armour: list[Armour] = []
        self.weapon: Weapon | None = None
        self.potion: Potion | None = None

    def get_protection(self) -> int:
        """Returns the knight's protection points"""
        armour_protection = sum(map(
            lambda armour: armour.protection,
            self.armour
        ))
        return self.protection + armour_protection

    def get_attack_damage(self) -> int:
        """Returns the knight's power points"""
        return self.power + self.weapon.power

    def hurt(self, damage: int) -> None:
        """Deals damage to the knight, taking into account his protection"""
        damage -= self.get_protection()

        if damage >= self.hp:
            self.hp = 0
            return

        self.hp -= damage

    def apply_boosts(self) -> None:
        """Applies potions and other boosts"""
        if self.potion:
            for effect_name, effect_delta in self.potion.effect.items():
                if hasattr(self, effect_name):
                    value = getattr(self, effect_name)
                    value += effect_delta
                    setattr(self, effect_name, value)

            self.potion = None
