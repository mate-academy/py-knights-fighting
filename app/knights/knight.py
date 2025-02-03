from __future__ import annotations
from app.items.apparel import Apparel
from app.items.weapon import Weapon
from app.items.potion import Potion
from app.items.gear_set import GearSet


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def suit_up(self, gear: GearSet) -> None:
        self.equip_weapon(gear.weapon)
        self.put_on_protective_gear(gear.apparel)
        self.drink_potions(gear.potions)

    def put_on_protective_gear(self, apparel_list: list[Apparel]) -> None:
        for apparel in apparel_list:
            self.protection += apparel.pro

    def equip_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def drink_potions(self, potions: list) -> None:
        for potion in potions:
            self.apply_potion_effect(potion)

    def apply_potion_effect(self, potion: Potion) -> None:
        for effect in potion.effects:
            attr_value = self.__getattribute__(effect.effect_name)
            self.__setattr__(effect.effect_name, attr_value + effect.value)

    def strike(self, opponent: Knight) -> None:
        opponent.hp -= self.power - opponent.protection

    def is_defeated(self) -> bool:
        return self.hp <= 0
