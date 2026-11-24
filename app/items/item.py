from abc import ABC


class Item(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
