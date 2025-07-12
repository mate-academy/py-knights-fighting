from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: Armour,
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self._name = name
        self._weapon = weapon
        self._potion = potion
        self._armour = armour
        self._power = power + self._weapon.power + self._potion.power
        self._hp = hp + self._potion.hp
        self._protection = self._armour.protection + self._potion.protection

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        value = max(0, value)
        self._hp = value

    @property
    def protection(self) -> int:
        return self._protection

    @property
    def power(self) -> int:
        return self._power

    @property
    def name(self) -> str:
        return self._name

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    @property
    def armour(self) -> Armour:
        return self._armour

    @property
    def potion(self) -> Potion:
        return self._potion
