def apply_armour(knights_data: dict) -> dict:
    for knight in knights_data.values():
        knight["protection"] = 0
        for armour in knight["armour"]:
            knight["protection"] += armour["protection"]
    return knights_data
