from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.person.knight import Knight


class Armour:
    def __init__(self, armour: list | None, protection: int = 0) -> None:
        self.armour = armour
        self.protection = protection

    def apply(self, knight: "Knight") -> None:
        knight.protection += self.protection
