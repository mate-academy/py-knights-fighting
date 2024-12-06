from app.adapters.item_adapter import ItemAdapter


class InventoryAdapter:
    def __init__(self, config):
        self.item_datas = ItemAdapter.extract_item_datas(config)
