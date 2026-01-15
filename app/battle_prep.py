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
            for attribute, value in knight.potion["effect"].items():
                if attribute == "power":
                    knight.power += value
                elif attribute == "protection":
                    knight.protection += value
                elif attribute == "hp":
                    knight.hp += value
