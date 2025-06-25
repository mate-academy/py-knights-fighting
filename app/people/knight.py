from __future__ import annotations

from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon,
        armours: list[Armour] = None,
        potion: Potion = None,
        protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armours = armours
        self.potion = potion
        self.protection = protection

    def __repr__(self) -> str:
        return (
            f"Knight(\n"
            f"\tname = '{self.name}',\n"
            f"\tpower = {self.power},\n"
            f"\thp = {self.hp},\n"
            f"\tweapon = {self.weapon},\n"
            f"\tarmours = {self.armours},\n"
            f"\tpotion = {self.potion}\n"
            f"\tprotection = {self.protection}\n"
            f")"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def create_from_dict(cls, data: dict) -> Knight | None:
        if not data:
            return None

        name = data.get("name", "")
        power = data.get("power", 0)
        hp = data.get("hp", 0)
        weapon = Weapon.create_from_dict(data.get("weapon", {}))
        armours = [
            Armour.create_from_dict(armor)
            for armor in data.get("armour", [])
        ]
        potion = Potion.create_from_dict(data.get("potion", {}))
        protection = data.get("protection", 0)

        return cls(
            name,
            power,
            hp,
            weapon,
            armours if armours else None,
            potion,
            protection
        )

    def take_damage(self, damage: int) -> None:
        self.hp -= max(0, damage - self.protection)
        if self.hp < 0:
            self.hp = 0

    @staticmethod
    def battle(
        first_knight: Knight,
        second_knight: Knight
    ) -> None:
        first_knight.take_damage(second_knight.power)
        second_knight.take_damage(first_knight.power)

    def prepare_to_fight(self) -> None:
        if self.armours:
            self.protection = sum(
                armour.protection
                for armour in self.armours
            )

        if self.potion:
            self.power += self.potion.effect.power
            self.hp += self.potion.effect.hp
            self.protection += self.potion.effect.protection

        self.power += self.weapon.power
