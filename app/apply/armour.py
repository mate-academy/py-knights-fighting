def apply_armour(name: dict) -> None:
    name["protection"] = 0
    for armour in name["armour"]:
        name["protection"] += armour["protection"]
