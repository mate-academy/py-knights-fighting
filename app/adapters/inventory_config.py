from app.adapters.item_config import ItemConfig


class InventoryConfig:
    def __init__(
            self,
            knight_dict: dict[str, str | int | dict]
    ) -> None:
        self.weapon_datas = []
        self.armour_datas = []
        self.potion_datas = []
        self.item_datas = []

        self._assign_items(
            ItemConfig.extract_item_configs(knight_dict)
        )

    def _assign_items(self, item_configs: list[ItemConfig]) -> None:
        for item_config in item_configs:
            if item_config.type == "weapon":
                self.weapon_datas.append(item_config)

            if item_config.type == "potion":
                self.potion_datas.append(item_config)

            if item_config.type == "armour":
                self.armour_datas.append(item_config)

            if item_config.type == "item":
                self.item_datas.append(item_config)
