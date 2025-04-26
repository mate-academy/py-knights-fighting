def prepare_knight(knight: dict) -> dict:

    knight["protection"] = sum(armo["protection"] for armo in knight["armour"])

    knight["power"] += knight["weapon"]["power"]

    if knight.get("potion") and knight["potion"].get("effect"):
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] = knight.get(stat, 0) + value

    return knight
