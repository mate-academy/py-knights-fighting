def knights_preparing(knight: dict) -> None:

    knight["protection"] = 0

    if knight["armour"] is not []:
        for armour in knight["armour"]:
            knight["protection"] += armour["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        for enhancement in knight["potion"]["effect"].keys():
            knight[enhancement] += knight["potion"]["effect"][enhancement]
