from __future__ import annotations
from app.models.knight import Knight


class Armour:

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def apply(self, knight: Knight) -> None:
        knight.protection += self.protection
