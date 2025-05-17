from __future__ import annotations
from typing import cast

from adapters.effect_config import EffectConfig
from config_dicts.knights_dicts import KnightDictType


class ItemConfig:
    def __init__(
        self,
        item_dict: dict[str, int | str | dict[str, int | str]],
        item_type: str = "item",
    ) -> None:
        self.type = item_type

        if item_dict.get("name", None):
            self.name = str(item_dict.get("name"))
        elif item_dict.get("part", None):
            self.name = str(item_dict.get("part"))

        self.effect_data = EffectConfig(item_dict)

    @classmethod
    def extract_item_configs(cls, knight_dict: KnightDictType) -> list[ItemConfig]:
        """
        Function to construct multiple ItemConfigs from dictionary

        :param item_dicts: dictionary of the form "item_type": {}
        :return: list of ItemConfig objects
        """
        item_configs: list[ItemConfig] = []

        for key, value in knight_dict.items():
            if key == "weapon" and value is not None:
                item_configs.append(
                    cls(
                        cast(dict[str, int | str | dict[str, int | str]], value),
                        "weapon",
                    )
                )

            if key == "potion" and value is not None:
                item_configs.append(
                    cls(
                        cast(dict[str, int | str | dict[str, int | str]], value),
                        "potion",
                    )
                )

            if key == "armour" and value is not None:
                value = cast(list[dict[str, str | int]], value)
                for armour_piece in value:
                    item_configs.append(
                        cls(
                            cast(
                                dict[str, int | str | dict[str, int | str]],
                                armour_piece,
                            ),
                            "armour",
                        )
                    )

        return item_configs
