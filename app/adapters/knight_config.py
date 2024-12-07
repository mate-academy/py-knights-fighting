from __future__ import annotations

from app.adapters.inventory_config import InventoryConfig


class KnightConfig:
    def __init__(self, knight_dict: dict[str, str | int | dict]) -> None:
        self.name = str(knight_dict.get("name"))
        self.power = int(knight_dict.get("power", 0))
        self.hp = int(knight_dict.get("hp", 0))
        self.protection = 0

        self.inventory_data = InventoryConfig(knight_dict)

    @classmethod
    def extract_knight_configs(
            cls,
            knight_dicts: dict[str, dict]
    ) -> list[KnightConfig]:
        """
        Method to construct a list of KnightConfigs from a dict

        :param knight_dicts: dict of knights
        :return: list of KnightConfig objects
        """

        knight_configs = []

        for knight_dict in knight_dicts.values():
            knight_configs.append(cls(knight_dict))

        return knight_configs
