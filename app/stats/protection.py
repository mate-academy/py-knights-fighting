def protection(name: dict) -> None:
    name["protection"] = 0
    for prot in name["armour"]:
        name["protection"] += prot["protection"]
