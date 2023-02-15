from __future__ import annotations

from app.ammunition.armour import Armour
from app.ammunition.potion import Potion
from app.ammunition.weapon import Weapon


class Knight:
    _all_knights = []

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: [Armour],
            weapon: Weapon,
            potion: Potion,
    ) -> None:

        self._name = name
        self._hp = hp
        self._power = power
        self._protection = 0
        self._weapon = weapon
        self._armour = armour
        self._potion = potion
        self.prepare_for_battle()

        Knight._all_knights.append(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def power(self) -> int:
        return self._power

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def protection(self) -> int:
        return self._protection

    @property
    def armour(self) -> [Armour]:
        return self._armour

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    @property
    def potion(self) -> [Potion]:
        return self._potion

    def _apply_armour(self) -> None:
        self._protection += sum(armour.protection
                                for armour in self._armour)

    def _apply_potion(self) -> None:
        for effect in self.potion.effect:
            protected_effect = "_" + effect
            new_value = (getattr(self, protected_effect)
                         + self.potion.effect[effect])
            setattr(self, protected_effect, new_value)

    def _appy_weapon(self) -> None:
        self._power += self._weapon.power

    def prepare_for_battle(self) -> None:
        self._apply_armour()
        self._appy_weapon()
        try:
            self._apply_potion()
        except AttributeError:
            pass

    def hit(self, other: Knight) -> None:
        if self._power >= other._protection + other._hp:
            other._protection = 0
            other._hp = 0

        elif self._power >= other._protection:
            other._hp -= self._power - other._protection
            other._protection = 0

    @classmethod
    def get_hp_all_knights(cls) -> dict[str: int]:
        return {knight._name: knight._hp for knight in cls._all_knights}
