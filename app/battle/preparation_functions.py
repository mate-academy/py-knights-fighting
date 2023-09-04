from app.knights.knight_class import Knight


def apply_armour(knight: Knight) -> None:
    for armour in knight.armour:
        knight.protection += armour["protection"]


def apply_weapon(knight: Knight) -> None:
    knight.power += knight.weapon["power"]


def apply_potion(knight: Knight) -> None:

    if knight.potion is not None:
        if "power" in knight.potion["effect"]:
            knight.power += knight.potion["effect"]["power"]

        if "protection" in knight.potion["effect"]:
            knight.protection += knight.potion["effect"]["protection"]

        if "hp" in knight.potion["effect"]:
            knight.hp += knight.potion["effect"]["hp"]
