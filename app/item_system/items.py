from __future__ import annotations

from app.adapters.item_config import ItemConfig
from app.item_system.effect import Effect


class Item:
    def __init__(self, item_data: ItemConfig) -> None:
        self.name = item_data.name
        self._effect = Effect(item_data.effect_data)

    def __str__(self) -> str:
        return f"{self.name}({self.effect})"

    def __eq__(self, other: Item) -> bool:
        return (
            self.name == other.name
            and self.effect == other.effect
        )

    def __lt__(self, other: Item) -> bool:
        return self.effect < other.effect

    def __gt__(self, other: Item) -> bool:
        return self.effect > other.effect

    @property
    def effect(self):
        return self._effect

    @classmethod
    def make_items(cls, item_datas: list[ItemConfig]):
        for item_data in item_datas:
            yield cls(item_data)

class Armour(Item):
    def __init__(self, item_data: ItemConfig) -> None:
        super().__init__(item_data)

    def __str__(self):
        return "Armour " + super().__str__()


class Potion(Item):
    def __init__(self, item_data: ItemConfig) -> None:
        super().__init__(item_data)

    def __str__(self):
        return super().__str__()


class Weapon(Item):
    def __init__(self, item_data: ItemConfig) -> None:
        super().__init__(item_data)

    def __str__(self):
        return super().__str__()
