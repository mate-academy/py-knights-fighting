def prepare(knight: dict) -> dict:
    knight["protection"] = sum(a["protection"] for a in knight["armour"])
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"]:
        knight.update({key: knight[key] + value
                       for key, value in knight["potion"]["effect"].items()})

    return knight
