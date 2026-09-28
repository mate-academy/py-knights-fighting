from __future__ import annotations

from app.knights.equipment import Armour, Potion, Weapon


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon,
        armour: list[Armour] | None = None,
        potion: Potion | None = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.weapon = weapon
        self.armour = armour or []
        self.potion = potion

    @classmethod
    def from_dict(cls, data: dict) -> Knight:
        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            weapon=Weapon.from_dict(data["weapon"]),
            armour=[Armour.from_dict(part) for part in data["armour"]],
            potion=Potion.from_dict(data["potion"]),
        )

    @property
    def is_defeated(self) -> bool:
        return self.hp == 0

    def prepare_for_battle(self) -> None:
        self.protection = sum(part.protection for part in self.armour)
        self.power += self.weapon.power
        if self.potion is not None:
            self.drink(self.potion)

    def drink(self, potion: Potion) -> None:
        self.hp += potion.effect.get("hp", 0)
        self.power += potion.effect.get("power", 0)
        self.protection += potion.effect.get("protection", 0)

    def take_hit(self, attacker: Knight) -> None:
        self.hp = max(self.hp - (attacker.power - self.protection), 0)

    def __repr__(self) -> str:
        return (
            f"Knight(name={self.name!r}, hp={self.hp}, "
            f"power={self.power}, protection={self.protection})"
        )
