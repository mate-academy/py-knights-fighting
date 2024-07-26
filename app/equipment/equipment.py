from abc import ABC, abstractmethod
from app.human.knight import Knight


class Equipment(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, knight: Knight) -> None:
        pass
