from __future__ import annotations


class Knight:

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def set_armour(self) -> None:
        if self.armour:
            for equipment in self.armour:
                self.protection += equipment.get("protection")

    def set_weapon(self) -> None:
        self.power += self.weapon.get("power")

    def set_potion(self) -> None:
        if self.potion:
            for effect, value in self.potion.get("effect").items():
                setattr(self, effect, getattr(self, effect) + value)

    def prepare(self) -> None:
        self.set_armour()
        self.set_weapon()
        self.set_potion()

    @staticmethod
    def fight(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection
        if first_knight.hp <= 0:
            first_knight.hp = 0
        if second_knight.hp <= 0:
            second_knight.hp = 0
