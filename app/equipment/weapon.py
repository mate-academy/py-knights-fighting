from typing import Any


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def apply(self, knight: Any) -> None:
        knight.power += self.power
