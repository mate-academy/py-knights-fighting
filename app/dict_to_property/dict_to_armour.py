from app.knight_properties.armour import Armour


def dict_to_armour(value: dict) -> list[Armour]:
    armour = []
    if len(value["armour"]):
        for armour_item in value["armour"]:
            armour.append(Armour(armour_item["part"],
                                 armour_item["protection"]))
    return armour
