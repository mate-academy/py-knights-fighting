from abc import ABC, abstractmethod
from typing import Any


class Equipment(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def apply(self, knight: Any) -> None:
        pass
