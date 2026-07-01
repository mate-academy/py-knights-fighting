def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        for attr, value in knight["potion"]["effect"].items():
            knight[attr] += value
