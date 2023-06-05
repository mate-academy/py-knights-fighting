from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armor(self, armour: Armour) -> None:
        print(f"{self.name} wears {armour.armour_part}")
        self.protection += armour.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        print(f"{self.name} takes {weapon.weapon_name}")
        self.power += weapon.weapon_power

    def use_potion(self, potion: Potion) -> None:
        print(f"{self.name} uses {potion.name}")
        self.hp += potion.hp
        self.power += potion.power
        self.protection += potion.protection

    def check_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0


class Weapon:
    def __init__(self, weapon_name: str, weapon_power: int) -> None:
        self.weapon_name = weapon_name
        self.weapon_power = weapon_power


class Armour:
    def __init__(self,
                 armour_part: str,
                 protection: int) -> None:
        self.armour_part = armour_part
        self.protection = protection


class Potion:
    def __init__(self,
                 name: str,
                 power: int = 0,
                 hp: int = 0,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
