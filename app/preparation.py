def get_ready_to_fight(knights_config: dict) -> dict:
    for knight in knights_config.values():
        knight["protection"] = sum(
            stats["protection"] for stats in knight["armour"]
        )

        knight["power"] += knight["weapon"]["power"]

        potion = knight.get("potion")
        if potion is not None:
            effects = potion.get("effect", {})
            knight["power"] += effects.get("power", 0)
            knight["protection"] += effects.get("protection", 0)
            knight["hp"] += effects.get("hp", 0)
    return dict(knights_config.items())
