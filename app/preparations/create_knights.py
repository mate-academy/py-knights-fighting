from __future__ import annotations
from app.preparations.knight import Knight


def create_dict_of_knights(knights_configuration: dict) -> dict:
    knights_dict = {
        name: Knight(
            parameters["name"],
            parameters["power"],
            parameters["hp"]
        ) for name, parameters in knights_configuration.items()
    }
    apply_equipment(knights_dict, knights_configuration)
    return knights_dict


def apply_equipment(knight_dict: dict, knights_configuration: dict) -> None:
    for name, parameters in knights_configuration.items():
        if parameters.get("armour"):
            knight_dict[name].apply_armour(parameters.get("armour"))
        if parameters.get("weapon"):
            knight_dict[name].apply_weapon(parameters.get("weapon"))
        if parameters.get("potion"):
            knight_dict[name].apply_potion(parameters.get("potion")["effect"])
