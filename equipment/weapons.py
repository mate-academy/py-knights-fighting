# app/equipment/weapons.py

class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self._name = name
        self._power = power

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, value: int) -> None:
        self._power = value
