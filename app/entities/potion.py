from __future__ import annotations


class Potion:
    def __init__(self,
                 name: str,
                 power: int = 0,
                 hp: int = 0,
                 protection: int = 0) -> None:
        self._name = name
        self._power = power
        self._hp = hp
        self._protection = protection

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Incorrect name")
        self._name = value

    @property
    def power(self) -> int:
        return self._power

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def protection(self) -> int:
        return self._protection

    @classmethod
    def from_dict(cls, data: dict) -> Potion:
        return cls(data["name"], **data["effect"])
