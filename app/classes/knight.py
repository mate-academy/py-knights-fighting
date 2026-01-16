from __future__ import annotations

from app.classes.weapon import Weapon
from app.classes.armour import Armour
from app.classes.potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: Weapon,
                 armour: list[Armour] = None,
                 potion: Potion = Potion("default_potion")) -> None:

        self.name = name

        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

    @property
    def total_hp(self) -> int:
        hp_for_battle = self.hp + self.potion.hp
        return hp_for_battle

    @property
    def total_power(self) -> int:
        power_for_battle = self.power + self.weapon.power + self.potion.power
        return power_for_battle

    @property
    def total_protection(self) -> int:
        protection_for_battle = self.potion.protection
        for armour in self.armour:
            protection_for_battle += armour.protection
        return protection_for_battle

    def fight(self, opponent: Knight) -> None:
        get_damage = (opponent.total_power
                      - self.total_protection)
        if get_damage > self.potion.hp:
            self.hp -= get_damage - self.potion.hp
            self.potion.hp = 0
            self.hp = max(self.hp, 0)
        else:
            self.potion.hp -= get_damage
