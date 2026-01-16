from __future__ import annotations
from app.entities.armour import Armour
from app.entities.potion import Potion
from app.entities.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int) -> None:
        self._name = name
        self._power = power
        self._hp = hp
        self._armour = []
        self._potion = None
        self._weapon = None
        self._protection = 0

    @property
    def is_alive(self) -> bool:
        return self._hp <= 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def protection(self) -> int:
        return self._protection

    @property
    def power(self) -> int:
        return self._power

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        if value < 0:
            self._hp = 0
        else:
            self._hp = value

    def setup_armour_from_dicts(self, data: list[dict]) -> None:
        if not data:
            return
        for part_armor in data:
            self._armour.append(Armour.from_dict(part_armor))
            self._protection += part_armor["protection"]

    def setup_potion_from_dict(self, data: dict) -> None:
        if data:
            self._potion = Potion.from_dict(data)

    def setup_weapon_from_dict(self, data: dict) -> None:
        if data:
            self._weapon = Weapon.from_dict(data)
            self._power += data["power"]

    @classmethod
    def from_dict(cls, data: dict) -> Knight:
        knight = Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
        )
        knight.setup_armour_from_dicts(data["armour"])
        knight.setup_potion_from_dict(data["potion"])
        knight.setup_weapon_from_dict(data["weapon"])
        return knight

    def apply_potion(self) -> None:
        if not self._potion:
            return
        self._hp += self._potion.hp
        self._protection += self._potion.protection
        self._power += self._potion.power

    def attack(self, opponent: Knight) -> None:
        damage = (self.power - opponent.protection)
        opponent.hp = opponent.hp - damage
