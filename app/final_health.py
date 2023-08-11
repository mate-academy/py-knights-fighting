def final_health(knights_dict: dict) -> dict:
    for knight in knights_dict.values():
        if knight["hp"] <= 0:
            knight["hp"] = 0
    return knights_dict
