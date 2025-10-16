from typing import Any


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def apply(self, knight: Any) -> None:
        knight.protection += self.protection
