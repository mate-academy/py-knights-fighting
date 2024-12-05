from app.data.item_data import ItemData
from app.items.item import Item


class Weapon(Item):
    def __init__(self, item_data: ItemData):
        super().__init__(item_data)
        self.effect = {"power": item_data.power}

    def __str__(self):
        return f"{super().__str__()}({self.effect})"
