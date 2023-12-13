from knights_class import Knight


def attribute_calculation(knight_warior: list[Knight]) -> list[Knight]:
    result_list = []

    for knight in knight_warior:
        if knight.armour:
            for detail_armour in knight.armour:
                knight.protection += detail_armour["protection"]

        knight.power += knight.weapon["power"]

        if knight.potion:
            for attribute, effect_value in knight.potion["effect"].items():
                setattr(
                    knight,
                    attribute,
                    getattr(knight, attribute) + effect_value)

        result_list.append(knight)

    return result_list
