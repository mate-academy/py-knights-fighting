from adapters.item_config import ItemConfig
from config_dicts.knights_dicts import KnightDictType


class InventoryConfig:
    def __init__(self, knight_dict: KnightDictType) -> None:
        self.weapon_datas: list[ItemConfig] = []
        self.armour_datas: list[ItemConfig] = []
        self.potion_datas: list[ItemConfig] = []
        self.item_datas: list[ItemConfig] = []

        self._assign_items(ItemConfig.extract_item_configs(knight_dict))

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
