from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.person.knight import Knight


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def apply(self, knight: "Knight") -> None:
        knight.power += self.power
