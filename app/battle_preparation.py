from app.knight_class import Knight


def battle_preparation(knight: Knight, knight_dict: dict) -> object:
    knight.protection += sum([_["protection"] for _ in knight_dict["armour"]])
    knight.power += knight_dict["weapon"]["power"]

    if knight_dict["potion"]:
        for effect, value in knight_dict["potion"]["effect"].items():
            setattr(knight, effect, getattr(knight, effect) + value)
    return knight
