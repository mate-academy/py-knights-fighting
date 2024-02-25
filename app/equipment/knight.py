from __future__ import annotations

from app.helpers.types import Effect
from app.helpers.custom_errors import MaxLevelError


class ArmourComponent:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect


class Weapon:
    def __init__(
        self,
        name: str,
        power: int,
        level: int = 0,
        max_level: int = 20
    ) -> None:
        self.name = name
        self.power = power
        self.level = level
        self.max_level = max_level

    def upgrade(self) -> None:
        if self.level == self.max_level:
            raise MaxLevelError(self.max_level)
        self.level += 1
        self.power += 50
