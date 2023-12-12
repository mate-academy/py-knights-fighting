from knights_class import Knight


def attribute_calculation(knight_warior: list[Knight]) -> list[Knight]:
    result_list = []

    for knight in knight_warior:
        if knight.armour:
            for detail_armour in knight.armour:
                knight.protection += detail_armour["protection"]

        knight.power += knight.weapon["power"]

        if knight.potion:
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]

            if "hp" in knight.potion["effect"]:
                knight.hp += knight.potion["effect"]["hp"]

            if "protection" in knight.potion["effect"]:
                knight.protection += knight.potion["effect"]["protection"]

        result_list.append(knight)

    return result_list
