from __future__ import annotations


class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self._name = name
        self._protection = protection

    @property
    def protection(self) -> int:
        return self.protection

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> name:
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @protection.setter
    def protection(self, protection: int) -> name:
        if protection < 0:
            raise ValueError("Invalid protection")
        self._protection = protection

    @classmethod
    def from_dict(cls, data: dict) -> Armour:
        return cls(data["part"], data["protection"])
