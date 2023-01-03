from __future__ import annotations
from app.knight import Knight


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def apply_armour(self, knight: Knight) -> None:
        knight.protection += self.protection
