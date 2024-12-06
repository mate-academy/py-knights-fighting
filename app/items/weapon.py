from app.adapters.item_adapter import ItemAdapter
from app.items.item import Item


class Weapon(Item):
    def __init__(self, item_data: ItemAdapter) -> None:
        super().__init__(item_data)
