from app.data.item_data import ItemData


class Item:
    def __init__(self, item_data: ItemData):
        self.name = item_data.name

    def __str__(self):
        return f"Item {self.name}"
