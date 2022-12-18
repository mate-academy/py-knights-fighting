from app.pkg.class_knights import Knight


def preparations(knights: dict) -> dict:
    knights_dict = {}

    for knight_name, knight in knights.items():
        knight["protection"] = 0

        for armour in knight["armour"]:
            knight["protection"] += armour["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:
            for char in ["power", "protection", "hp"]:
                knight[char] += knight["potion"]["effect"].get(char, 0)

        knights_dict[knight_name] = Knight(name=knight["name"],
                                           hp=knight["hp"],
                                           power=knight["power"],
                                           protection=knight["protection"])

    return knights_dict
