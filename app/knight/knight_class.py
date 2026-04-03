from __future__ import annotations

from typing import Any
from random import choice

from app.knight.knight_items_class import Armour, Weapon, Potion
from app.knight.contains import (FIRST_KNIGHT_INTROS, SECOND_KNIGHT_INTROS,
                                 ARMOUR_EQUIP_PHRASES, WEAPON_EQUIP_PHRASES,
                                 POTION_DRINK_PHRASES, KNIGHT_STATS_PHRASES,
                                 BATTLE_START_PHRASES, VICTORY_PHRASES)


class Knight:

    def __init__(self, dict_of_knight: dict[str, Any]) -> None:
        self.name: str = dict_of_knight.get("name")
        self.power: int = dict_of_knight.get("power")
        self.hp: int = dict_of_knight.get("hp")
        self.protection: int = 0
        self.armours: list[dict] = dict_of_knight.get("armour")
        self.weapon: dict = dict_of_knight.get("weapon")
        self.potion: dict = dict_of_knight.get("potion")

    def apply_armours(self) -> None:
        if self.armours is None:
            return

        for arm in self.armours:
            armour = Armour(arm)

            phrase = choice(ARMOUR_EQUIP_PHRASES)
            print(phrase.format(name=self.name, defens=armour.protection,
                                armour=armour.part))

            self.protection += armour.protection

    def apply_weapon(self) -> None:
        if self.weapon is None:
            return

        weapon = Weapon(self.weapon)

        phrase = choice(WEAPON_EQUIP_PHRASES)
        print(phrase.format(name=self.name, power=weapon.power,
                            weapon_name=weapon.name))

        self.power += weapon.power

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        potion = Potion(self.potion)

        phrase = choice(POTION_DRINK_PHRASES)
        print(phrase.format(name=self.name, potion=potion.name,
                            power=potion.power, hp=potion.hp,
                            defens=potion.protection))

        self.hp += potion.hp
        self.power += potion.power
        self.protection += potion.protection

    def battle(self, other: Knight) -> None:
        if not isinstance(other, Knight):
            return

        phrase_for_first = choice(FIRST_KNIGHT_INTROS)
        print(phrase_for_first.format(name=self.name))

        phrase_for_second = choice(SECOND_KNIGHT_INTROS)
        print(phrase_for_second.format(name=other.name))

        print("\n")
        self.apply_armours()
        print()
        other.apply_armours()
        print("\n")
        self.apply_weapon()
        other.apply_weapon()
        print("\n")
        self.apply_potion()
        other.apply_potion()
        print("\n")

        phrase_for_first = choice(KNIGHT_STATS_PHRASES)
        print(phrase_for_first.format(name=self.name, power=self.power,
                                      hp=self.hp, protect=self.protection))

        phrase_for_second = choice(KNIGHT_STATS_PHRASES)
        print(phrase_for_second.format(name=other.name, power=other.power,
                                       hp=other.hp, protect=other.protection))

        print("\n")
        phrase = choice(BATTLE_START_PHRASES)
        print(phrase.format(name1=self.name, name2=other.name))
        print("\n")

        self_damage = self.power - other.protection
        other_damage = other.power - self.protection
        self.hp = max(0, self.hp - other_damage)
        other.hp = max(0, other.hp - self_damage)

        phrase = choice(VICTORY_PHRASES)
        if self.hp > other.hp:
            print(phrase.format(name=self.name))
        elif other.hp > self.hp:
            print(phrase.format(name=other.name))
