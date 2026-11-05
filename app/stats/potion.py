def apply_potion(knight: dict) -> dict:
    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value
    return knight
