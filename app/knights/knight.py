from dataclasses import dataclass

from app.knights.items.weapon import Weapon
from app.knights.items.armour import Armour
from app.knights.items.potion import Potion


@dataclass
class Knight:
    name: str
    power: int
    armour: list | None
    weapon: Weapon
    hp: int
    potion: Potion = None
    protection: int = 0

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        if value <= 0:
            self._hp = 0
        else:
            self._hp = value

    def __post_init__(self) -> None:
        self.__apply_stats()

    @classmethod
    def from_dict(cls, knight: dict) -> "Knight":
        return cls(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=Armour.create(knight),
            weapon=Weapon.create(knight),
            potion=Potion.create(knight)
        )

    def __apply_stats(self) -> None:
        self.power += self.weapon.power

        if self.armour:
            for armour in self.armour:
                self.protection += armour.protection

        if self.potion:
            self.hp += self.potion.effect.hp
            self.protection += self.potion.effect.protection
            self.power += self.potion.effect.power

    @staticmethod
    def fight(first_knight: "Knight", second_knight: "Knight") -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection
