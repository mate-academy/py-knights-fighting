def battle_preparation(knight: dict) -> dict:

    # apply armour
    knight["protection"] = 0
    for armour in knight.get("armour"):
        if armour.get("protection"):
            knight["protection"] += armour.get("protection")

    # apply weapon
    knight["power"] += knight.get("weapon").get("power")

    # apply potion if exist
    potion = knight.get("potion")

    if potion:
        knight["power"] += (
            knight.get("potion").
            get("effect").
            get("power")
        ) if "power" in potion.get("effect") else 0
        knight["hp"] += (
            knight.get("potion").
            get("effect").
            get("hp")
        ) if "hp" in potion.get("effect") else 0
        knight["protection"] += (
            knight.get("potion").
            get("effect").
            get("protection")
        ) if "protection" in potion.get("effect") else 0

    return knight
