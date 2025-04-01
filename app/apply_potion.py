def apply_potion_if_exists(name: dict) -> None:
    if name.get("potion"):
        effects = name["potion"]["effect"]
        if "power" in effects:
            name["power"] += effects["power"]

        if "protection" in effects:
            name["protection"] += effects["protection"]

        if isinstance(effects["hp"], (int, float)):
            name["hp"] += effects["hp"]
