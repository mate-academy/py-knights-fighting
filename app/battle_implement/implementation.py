from __future__ import annotations

from app.entities.knight import Knight
from app.entities.stuff import Weapon, ArmourPart, SetArmourScope, Potion


def crete_armour(armours: list) -> SetArmourScope | list:
    if armours:
        armour_parts = [ArmourPart(armour.get("part"),
                                   armour.get("protection"))
                        for armour in armours]
        armour_scope = SetArmourScope(armour_parts)
        armour_scope.protection_level = armour_scope.calc_protection_level()
        return armour_scope
    return SetArmourScope([])


def create_weapon(weapon: dict) -> Weapon:
    name = weapon.get("name")
    power = weapon.get("power")
    return Weapon(name=name, power=power)


def create_potion(potion: dict | None) -> Potion | None:
    if potion:
        name = potion.get("name")
        effect = potion.get("effect")
        return Potion(name=name, effect=effect)


def create_knight(knight_info: dict) -> Knight:
    name = knight_info.get("name")
    power = knight_info.get("power")
    hp = knight_info.get("hp")
    armour_scope = crete_armour(knight_info.get("armour"))
    weapon = create_weapon(knight_info.get("weapon"))
    potion = create_potion(knight_info.get("potion"))
    knight = Knight(name=name,
                    power=power, hp=hp,
                    armour=armour_scope,
                    weapon=weapon,
                    potion=potion)
    return knight
