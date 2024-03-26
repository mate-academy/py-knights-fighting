from __future__ import annotations

from app.consts.parametrs import CHANGABLE


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection


class Poison:
    def __init__(self, name: str, effects: dict) -> None:
        self.name = name
        for effect in CHANGABLE:
            setattr(self, effect, effects.get(effect, 0))


class Knight:
    current_fight = 0

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

        self.armour = []
        for armour_part in knight["armour"]:
            self.armour.append(Armour(armour_part["part"],
                                      armour_part["protection"]))

        self.weapon = Weapon(knight["weapon"]["name"],
                             knight["weapon"]["power"])

        if knight["potion"]:
            self.potion = Poison(knight["potion"]["name"],
                                 knight["potion"]["effect"])

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = 0 if value < 0 else value

    def get_all_power(self) -> int:
        return (self.power + self.weapon.power
                + getattr(getattr(self, "potion", 0), "power", 0))

    def get_all_protection(self) -> int:
        protection = self.protection
        protection += sum(armour.protection for armour in self.armour)
        protection += getattr(getattr(self, "potion", 0), "protection", 0)
        return protection

    def fight(self, other: Knight) -> None:
        self.current_fight += 1
        self.hp += (getattr(getattr(self, "potion", 0), "hp", 0)
                    + self.get_all_protection()
                    - other.get_all_power())
        if self.current_fight + other.current_fight < 2:
            other.fight(self)
