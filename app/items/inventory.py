from app.adapters.InventoryAdapter import InventoryAdapter
from app.items.item import Item


class Inventory:
    def __init__(self, inventory_data: InventoryAdapter):
        self.items = list(Item.make_items(inventory_data.item_datas))

    def add(self, item: Item):
        ...

    def remove(self, item: Item):
        ...

