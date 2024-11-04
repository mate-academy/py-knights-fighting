from typing import Dict, Any


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:

    for knight_key, knight_data in knights_config.items():
        knight_data["protection"] = sum(
            armour["protection"] for armour in knight_data["armour"]
        )
        knight_data["power"] += knight_data["weapon"]["power"]
        if knight_data["potion"] is not None:
            knight_data["hp"] += knight_data["potion"]["effect"].get("hp", 0)
            knight_data["power"] +=\
                knight_data["potion"]["effect"].get("power", 0)
            knight_data["protection"] += knight_data["potion"]["effect"].get(
                "protection", 0
            )

    knights_config["ukraine"]["hp"] -= (
        knights_config["iran"]["power"]
        - knights_config["ukraine"]["protection"]
    )
    knights_config["iran"]["hp"] -= (
        knights_config["ukraine"]["power"]
        - knights_config["iran"]["protection"]
    )

    knights_config["china"]["hp"] -= (
        knights_config["russia"]["power"]
        - knights_config["china"]["protection"]
    )
    knights_config["russia"]["hp"] -= (
        knights_config["china"]["power"]
        - knights_config["russia"]["protection"]
    )

    for knight in ["ukraine", "china", "russia", "iran"]:
        if knights_config[knight]["hp"] < 0:
            knights_config[knight]["hp"] = 0

    return {
        knights_config["ukraine"]["name"]: knights_config["ukraine"]["hp"],
        knights_config["china"]["name"]: knights_config["china"]["hp"],
        knights_config["russia"]["name"]: knights_config["russia"]["hp"],
        knights_config["iran"]["name"]: knights_config["iran"]["hp"],
    }
