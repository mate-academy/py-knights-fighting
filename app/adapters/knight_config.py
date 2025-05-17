from __future__ import annotations

from adapters.inventory_config import InventoryConfig
from config_dicts.knights_dicts import KnightDictsType, KnightDictType


class KnightConfig:
    def __init__(self, knight_dict: KnightDictType) -> None:
        self.name = str(knight_dict.get("name"))
        self.power = int(str(knight_dict.get("power", 0)))
        self.hp = int(str(knight_dict.get("hp", 0)))
        self.protection = 0

        self.inventory_data = InventoryConfig(knight_dict)

    @classmethod
    def extract_knight_configs(
        cls, knight_dicts: KnightDictsType
    ) -> list[KnightConfig]:
        """
        Method to construct a list of KnightConfigs from a dict

        :param knight_dicts: dict of knights
        :return: list of KnightConfig objects
        """

        knight_configs: list[KnightConfig] = []

        for knight_dict in knight_dicts.values():
            knight_configs.append(cls(knight_dict))

        return knight_configs
