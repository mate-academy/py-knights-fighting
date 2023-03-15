from app.knight_class import Knight


def battle_preparation(knight: Knight, knight_dict: dict) -> object:
    knight.protection += sum([_["protection"] for _ in knight_dict["armour"]])
    knight.power += knight_dict["weapon"]["power"]
    if knight_dict["potion"]:
        knight.power += knight_dict["potion"]["effect"]["power"]
        knight.hp += knight_dict["potion"]["effect"]["hp"]
        knight.protection += \
            knight_dict["potion"]["effect"].get("protection", 0)

    return knight
