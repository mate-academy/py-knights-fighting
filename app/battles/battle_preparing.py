from typing import Any


def battle(knight_config: dict) -> Any:
    dict_updated = {}
    for knight_name, knight_info in knight_config.items():
        updated_warrior = knight_info.copy()
        updated_warrior["protection"] = 0
        for armor in updated_warrior["armour"]:
            updated_warrior["protection"] += armor["protection"]
        updated_warrior["power"] += updated_warrior["weapon"]["power"]

        if updated_warrior["potion"] is not None:
            potion_effect = updated_warrior["potion"]["effect"]
            if "power" in potion_effect:
                updated_warrior["power"] += potion_effect["power"]
            if "protection" in potion_effect:
                updated_warrior["protection"] += potion_effect["protection"]
            if "hp" in potion_effect:
                updated_warrior["hp"] += potion_effect["hp"]

        dict_updated[knight_name] = updated_warrior
    return dict_updated
