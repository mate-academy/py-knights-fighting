from typing import Any


def lancelot_preparation(knight_config: dict[str, Any]) -> dict:
    lancelot = knight_config["lancelot"]

    lancelot["protection"] = 0
    for armour in lancelot["armour"]:
        lancelot["protection"] += armour["protection"]

    lancelot["power"] += lancelot["weapon"]["power"]

    if lancelot["potion"] is not None:
        if "power" in lancelot["potion"]["effect"]:
            lancelot["power"] += lancelot["potion"]["effect"]["power"]

        if "protection" in lancelot["potion"]["effect"]:
            protect = lancelot["potion"]["effect"]["protection"]
            lancelot["protection"] += protect

        if "hp" in lancelot["potion"]["effect"]:
            lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

    return lancelot
