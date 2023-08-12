from app.knight_class import Knight


def apply_armour(knights: list[Knight]) -> None:
    for knight in knights:
        for clothes in knight.armour:
            knight.protection += clothes["protection"]


def apply_weapon(knights: list[Knight]) -> None:
    for knight in knights:
        knight.power += knight.weapon["power"]


def apply_potion(knights: list[Knight]) -> None:
    for knight in knights:
        if knight.potion is not None:
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]

            if "protection" in knight.potion["effect"]:
                knight.protection += knight.potion["effect"]["protection"]

            if "hp" in knight.potion["effect"]:
                knight.hp += knight.potion["effect"]["hp"]
