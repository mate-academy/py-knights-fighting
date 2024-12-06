from app.adapters.item_adapter import ItemAdapter
from app.items.effect import Effect


class Item:
    def __init__(self, item_data: ItemAdapter) -> None:
        self.name = item_data.name
        self.effect = Effect(item_data.effect_data)

    def __str__(self) -> str:
        return f"Item {self.name}"

    @staticmethod
    def make_items(item_datas: list[ItemAdapter]):
        for item_data in item_datas:
            yield Item(item_data)
