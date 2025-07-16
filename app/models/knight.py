from __future__ import annotations

from app.models.armour import Armour
from app.models.potion import Potion
from app.models.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: Weapon,
                 armour: list[Armour] = None,
                 potion: Potion = None,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.protection = protection
        self.armour = armour or []
        self.potion = potion

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for armour_el in self.armour:
            self.protection += armour_el.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        effect = self.potion.effect

        if effect.power:
            self.power += effect.power

        if effect.protection:
            self.protection += effect.protection

        if effect.hp:
            self.hp += effect.hp

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        self.check_if_fell()
        other.check_if_fell()

    @classmethod
    def from_dict(cls, data: dict) -> Knight | None:
        if not data:
            return None

        return cls(
            name=data.get("name"),
            power=data.get("power"),
            hp=data.get("hp"),
            weapon=Weapon.from_dict(data.get("weapon")),
            armour=Armour.from_dict_list(data.get("armour")),
            potion=Potion.from_dict(data.get("potion"))
        )

    def check_if_fell(self) -> None:
        if self.hp <= 0:
            self.hp = 0
