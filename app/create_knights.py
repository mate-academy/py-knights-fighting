from typing import Any

from app.knights import CreateKnights


def create_knights(dict_of_knights: dict) -> dict[str, CreateKnights]:
    knights: dict[Any, Any] = dict()
    new_dict = {}
    for value_knights in dict_of_knights.values():
        total_power: list[Any] = []
        total_protection: list[Any] = []
        total_hp: list[Any] = []

        total_power.append(value_knights["power"])
        total_power.append(value_knights["weapon"].get("power"))
        total_hp.append(value_knights["hp"])
        for knight_armors in value_knights["armour"]:
            total_protection.append(knight_armors["protection"])
        if value_knights["potion"] is not None:
            total_hp.append(value_knights["potion"]["effect"]["hp"])
            total_power.append(value_knights["potion"]["effect"]["power"])
            total_protection.append(value_knights["potion"]
                                    ["effect"].get("protection", 0))
        new_dict["power"] = sum(total_power)
        new_dict["protection"] = sum(total_protection)
        new_dict["hp"] = sum(total_hp)
        knights[value_knights["name"]] = CreateKnights(value_knights["name"],
                                                       new_dict["power"],
                                                       new_dict["protection"],
                                                       new_dict["hp"])

    return knights
