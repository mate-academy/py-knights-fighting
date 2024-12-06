from __future__ import annotations

from app.adapters.effect_config import EffectConfig


class ItemConfig:
    def __init__(self, config: dict[str, int | dict], item_type: str= "item") -> None:
        self.type = item_type
        if config.get("name", None):
            self.name = str(config.get("name"))
        elif config.get("part", None):
            self.name = str(config.get("part"))
        else:
            self.name = "Item"

        self.effect_data = EffectConfig(config)

    @staticmethod
    def extract_item_datas(config) -> list[ItemConfig]:
        item_datas = []
        for key, value in config.items():
            if key == "weapon" and value is not None:
                item_datas.append(ItemConfig(value, "weapon"))
            if key == "potion" and value is not None:
                item_datas.append(ItemConfig(value, "potion"))
            if key == "armour" and value is not None:
                for armour_piece in value:
                    item_datas.append(ItemConfig(armour_piece, "armour"))
        return item_datas
