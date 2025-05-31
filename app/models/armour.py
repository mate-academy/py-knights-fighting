from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.knight import Knight  # Импорт только для проверки типов


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def apply(self, knight: Knight) -> None:
        knight.protection += self.protection
