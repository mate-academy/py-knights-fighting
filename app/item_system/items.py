from __future__ import annotations
from typing import Generator

from adapters.item_config import ItemConfig
from item_system.effect import Effect


class Item:
    """
    Represents an Item

    Properties:
        name (str): item's name
        effect (Effect): item's Effect object, a buff or debuff item can give
    """

    def __init__(self, item_data: ItemConfig) -> None:
        self.name = item_data.name
        self._effect = Effect(item_data.effect_data)

    def __str__(self) -> str:
        return f"{self.name}({self.effect})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Item):
            return NotImplemented

        return self.name == other.name and self.effect == other.effect

    def __lt__(self, other: Item) -> bool:
        return self.effect < other.effect

    def __gt__(self, other: Item) -> bool:
        return self.effect > other.effect

    @property
    def effect(self) -> Effect:
        return self._effect

    @classmethod
    def make_items(cls, item_configs: list[ItemConfig]) -> Generator[Item, None, None]:
        """
        Pass ItemConfig from item_datas to Item constructor

        :param item_configs: list of ItemConfigs
        :return: generator of Item objects
        """
        for item_data in item_configs:
            yield cls(item_data)


class Armour(Item):
    def __init__(self, item_data: ItemConfig) -> None:
        super().__init__(item_data)

    def __str__(self) -> str:
        return "Armour " + super().__str__()


class Potion(Item):
    def __init__(self, item_data: ItemConfig) -> None:
        super().__init__(item_data)

    def __str__(self) -> str:
        return super().__str__()


class Weapon(Item):
    def __init__(self, item_data: ItemConfig) -> None:
        super().__init__(item_data)

    def __str__(self) -> str:
        return super().__str__()
