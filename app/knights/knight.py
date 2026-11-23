from __future__ import annotations

from app.knights.armour import Armour
from app.knights.potion import Potion
from app.knights.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            armour: list[Armour | None],
            potion: Potion | None = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.total_power = self.calculate_total_power()
        self.total_hp = self.calculate_total_hp()
        self.total_armour = self.calculate_total_armour()

    def calculate_total_power(self) -> int:
        bonus = 0
        if self.potion is not None:
            bonus = self.potion.effect.get("power", 0)
        result = self.power + self.weapon.power + bonus
        return int(result)

    def calculate_total_hp(self) -> int:
        bonus = 0
        if self.potion is not None:
            bonus = self.potion.effect.get("hp", 0)
        return int(self.hp + bonus)

    def calculate_total_armour(self):
        bonus_armour = 0
        if self.armour:
            for armour_ in self.armour:
                bonus_armour += armour_.protection
        if self.potion is not None:
            bonus_armour += self.potion.effect.get("protection", 0)
        return int(bonus_armour)

    def fight(self, opponent: "Knight") -> None:
        damage_to_opponent = max(0, self.total_power - opponent.total_armour)
        damage_to_self = max(0, opponent.total_power - self.total_armour)
        self.total_hp = max(0, self.total_hp - damage_to_self)
        opponent.total_hp = max(0, opponent.total_hp - damage_to_opponent)
