# app/equipment/armour.py

class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @property
    def part(self) -> str:
        return self._part

    @part.setter
    def part(self, value: str) -> None:
        self._part = value

    @property
    def protection(self) -> int:
        return self._protection

    @protection.setter
    def protection(self, value: int) -> None:
        self._protection = value
