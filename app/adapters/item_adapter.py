from __future__ import annotations

from app.adapters.effect_adapter import EffectAdapter


class ItemAdapter:
    def __init__(self, config: dict[str, int | dict]) -> None:
        if config.get("name", None):
            self.name = str(config.get("name"))
        elif config.get("part", None):
            self.name = str(config.get("part"))
        else:
            self.name = "Item"

        self.effect_data = EffectAdapter(config)

    @staticmethod
    def extract_item_datas(config) -> list[ItemAdapter]:
        item_datas = []
        for key, value in config.items():
            if key == "weapon" and value is not None:
                item_datas.append(ItemAdapter(value))
            if key == "potion" and value is not None:
                item_datas.append(ItemAdapter(value))
            if key == "armour" and value is not None:
                for armour_piece in value:
                    item_datas.append(ItemAdapter(armour_piece))
        return item_datas
