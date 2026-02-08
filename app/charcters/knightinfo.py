from __future__ import annotations
from app.charcters.armour import Armour
from app.charcters.weapon import Weapon
from app.charcters.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_equipment(self) -> None:
        self.protection = sum(a.protection for a in self.armour)
        self.power += self.weapon.power

    def prepare_for_battle(self) -> None:
        self.apply_equipment()
        if self.potion is not None:
            self.power += self.potion.power
            self.protection += self.potion.protection
            self.hp += self.potion.hp
        self.hp = max(0, self.hp)

    @classmethod
    def from_dict(cls, data: dict) -> Knight:
        weapon = Weapon(**data["weapon"])
        armour = [Armour(**a) for a in data["armour"]]
        potion = None
        if data.get("potion"):
            potion = Potion(
                name=data["potion"]["name"],
                **data["potion"]["effect"]
            )
        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=armour,
            weapon=weapon,
            potion=potion
        )
