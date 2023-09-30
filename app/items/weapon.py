from .item import Item


class Weapon(Item):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name, power, 0, 0)

    @classmethod
    def from_dict(cls, data: dict) -> "Weapon":
        return cls(data["name"], data["power"])
