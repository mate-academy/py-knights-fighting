from app.items.item import Item


class Armour(Item):
    def __init__(self, name: str, protection: int) -> None:
        super().__init__(name)
        self._protection = protection

    @property
    def protection(self) -> int:
        return self._protection

    @staticmethod
    def create_armour(config: dict) -> "Armour":
        return Armour(config["part"], config["protection"])
