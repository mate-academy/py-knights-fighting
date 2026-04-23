def apply_potion(knights_data: dict) -> dict:
    for knight in knights_data.values():
        if knight["potion"] is not None:
            for stat, value in knight["potion"]["effect"].items():
                knight[stat] += value
    return knights_data
