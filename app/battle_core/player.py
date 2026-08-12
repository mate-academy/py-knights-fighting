from typing import Dict


def prepare_knight(knight_config: Dict) -> Dict:
    # apply armour
    knight_config["protection"] = 0
    for armor in knight_config["armour"]:
        knight_config["protection"] += armor["protection"]

    # apply weapon
    weapon_power = knight_config["weapon"]["power"]
    knight_config["power"] += weapon_power

    # apply potion if exist
    if knight_config["potion"] is not None:
        effect = knight_config["potion"]["effect"]
        if "power" in effect:
            knight_config["power"] += effect["power"]

        if "protection" in effect:
            knight_config["protection"] += effect["protection"]

        if "hp" in effect:
            knight_config["hp"] += effect["hp"]

    return knight_config
