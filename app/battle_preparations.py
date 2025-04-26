def prepare_knight(knight: dict) -> dict:

    knight["protection"] = sum(armo["protection"] for armo in knight["armour"])

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"]:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value

    return knight
