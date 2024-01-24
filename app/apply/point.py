def apply_point(name: dict) -> None:
    if name.get("potion"):
        effect = name.get("potion").get("effect", {})
        name["power"] += effect.get("power", 0)
        name["protection"] += effect.get("protection", 0)
        name["hp"] += effect.get("hp", 0)
