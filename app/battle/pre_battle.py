def prepare_knights(knights_one: dict) -> dict:

    for knight in knights_one:
        knight = knights_one[knight]

        knight["protection"] = 0

        for armour_in in knight["armour"]:
            knight["protection"] += armour_in["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"]:
            for strength in knight["potion"]["effect"]:
                knight[strength] += knight["potion"]["effect"][strength]

    return knights_one
