def prepare_knight(knight: dict) -> dict:
    knight_copy = knight.copy()

    knight_copy["protection"] = sum(
        armo["protection"] for armo in knight_copy["armour"]
    )
    knight_copy["power"] += knight_copy["weapon"]["power"]

    if knight_copy.get("potion") and knight_copy["potion"].get("effect"):
        for stat, value in knight_copy["potion"]["effect"].items():
            knight_copy[stat] = knight_copy.get(stat, 0) + value

    return knight_copy
