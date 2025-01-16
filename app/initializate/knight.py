from __future__ import annotations
from app.stats.Head import Main
from app.stats.armour import Armour
from app.stats.potion import Potion
from app.stats.weapon import Weapon


class Knight:

    def __init__(self, main: Main, armour: Armour,
                 weapon: Weapon, potion: Potion) -> None:
        self.power = None
        self.hp = None
        self.protection = None
        self.main = main
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def __repr__(self) -> str:
        attributes = ", ".join(f"{key}={value!r}" for key, value
                               in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"

    def show_full_info(self) -> str:
        main_info = f"Main: {self.main}"
        armour_info = f"Armour: {self.armour}"
        weapon_info = f"Weapon: {self.weapon}"
        potion_info = f"Potion: {self.potion}"
        return (f"Knight Info: \n{main_info}\n{armour_info}"
                f"\n{weapon_info}\n{potion_info}")

    def show_fight_ready_knight(self) -> str:
        name = f"Name: {self.main.name}"
        power_info = f"Power: {self.power}"
        power_hp = f"Hp: {self.hp}"
        power_protection = f"Protection: {self.protection}"
        return f"{name}\n{power_info}\n{power_hp}\n{power_protection}\n"

    def prepare_to_fight(self) -> Knight:
        if self.potion.potion:
            self.power = (self.main.power + self.weapon.power
                          + self.potion.power)
            self.hp = (self.main.hp + self.potion.hp)
            self.protection = (self.main.protection
                               + self.armour.total_protection
                               + self.potion.protection)
        else:
            self.power = (self.main.power + self.weapon.power)
            self.hp = self.main.hp
            self.protection = (self.main.protection
                               + self.armour.total_protection)
        return self

    def attack(self, other_knight: Knight) -> dict:
        if not isinstance(other_knight, Knight):
            raise ValueError("should be other knight fighter")

        damage_to_other = max(0, self.power - other_knight.protection)
        damage_to_self = max(0, other_knight.power - self.protection)

        other_knight.hp = max(0, other_knight.hp - damage_to_other)
        self.hp = max(0, self.hp - damage_to_self)

        fight_result = {
            self.main.name: self.hp,
            other_knight.main.name: other_knight.hp
        }

        return fight_result
