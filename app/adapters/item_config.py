from __future__ import annotations

from app.adapters.effect_config import EffectConfig


class ItemConfig:
    def __init__(
            self,
            item_dict: dict[str, str | int | dict | None],
            item_type: str = "item"
    ) -> None:
        self.type = item_type

        if item_dict.get("name", None):
            self.name = str(item_dict.get("name"))
        elif item_dict.get("part", None):
            self.name = str(item_dict.get("part"))

        self.effect_data = EffectConfig(item_dict)

    @classmethod
    def extract_item_configs(
            cls,
            item_dicts: dict[str, list[dict] | dict | None]
    ) -> list[ItemConfig]:
        """
        Function to construct multiple ItemConfigs from dictionary

        :param item_dicts: dictionary of the form "item_type": {}
        :return: list of ItemConfig objects
        """

        item_configs = []

        for key, value in item_dicts.items():
            if key == "weapon" and value is not None:
                item_configs.append(cls(value, "weapon"))

            if key == "potion" and value is not None:
                item_configs.append(cls(value, "potion"))

            if key == "armour" and value is not None:
                for armour_piece in value:
                    item_configs.append(cls(armour_piece, "armour"))

        return item_configs
