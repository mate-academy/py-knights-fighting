def armour(knights_dict: dict) -> None:
    for key, knight in knights_dict.items():
        knight["protection"] = 0
        for arm in knight["armour"]:
            knight["protection"] += arm["protection"]
