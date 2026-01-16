from .item import Item


class Potion(Item):
    def __init__(self, name: str, effect: dict) -> None:
        power = effect["power"] if "power" in effect else 0
        hp = effect["hp"] if "hp" in effect else 0
        protection = effect["protection"] if "protection" in effect else 0

        super().__init__(name, power, hp, protection)

    @classmethod
    def from_dict(cls, data: dict) -> "Potion":
        return cls(data["name"], data["effect"])
