from app.items.item import Item
from app.data.item_data import ItemData


class Armour(Item):
    def __init__(self, item_data: ItemData):
        super().__init__(item_data)
        self.effect = {"protection": item_data.protection}

    def __str__(self):
        return f"{super().__str__()}({self.effect})"
