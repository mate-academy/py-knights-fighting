from app.items.item import Item


class Weapon(Item):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self._power = power

    @property
    def power(self) -> int:
        return self._power
