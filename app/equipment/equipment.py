from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.hero import Hero


class Equipment(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def apply_effect(self, hero: Hero) -> None:
        pass
