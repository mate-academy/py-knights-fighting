from typing import Any


def arthur_preparation(knight_config: dict[str, Any]) -> dict:
    arthur = knight_config["arthur"]

    arthur["protection"] = 0
    for armour in arthur["armour"]:
        arthur["protection"] += armour["protection"]

    arthur["power"] += arthur["weapon"]["power"]

    if arthur["potion"] is not None:
        if "power" in arthur["potion"]["effect"]:
            arthur["power"] += arthur["potion"]["effect"]["power"]

        if "protection" in arthur["potion"]["effect"]:
            arthur["protection"] += arthur["potion"]["effect"]["protection"]

        if "hp" in arthur["potion"]["effect"]:
            arthur["hp"] += arthur["potion"]["effect"]["hp"]

    return arthur
