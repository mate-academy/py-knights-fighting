from .item import Item


class Armour(Item):
    def __init__(self, name: str, protection: int) -> None:
        super().__init__(name, 0, 0, protection)

    @classmethod
    def from_dict(cls, data: dict) -> "Armour":
        return cls(data["part"], data["protection"])
