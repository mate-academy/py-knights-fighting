from app.items.item import Item
from app.adapters.item_adapter import ItemAdapter


class Armour(Item):
    def __init__(self, item_data: ItemAdapter) -> None:
        super().__init__(item_data)
