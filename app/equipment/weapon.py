from __future__ import annotations

from app.errors.upgrade import MaxLevelError


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

    def upgrade(self) -> Weapon | MaxLevelError:
        if self.level == self.max_level:
            raise MaxLevelError(self.max_level)
        self.level += 1
        self.power += 50
        return self
