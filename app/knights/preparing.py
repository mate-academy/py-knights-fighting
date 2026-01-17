from app.knights.knights_init import Knight


def preparation_knight(knight: Knight) -> Knight:
    # apply armour
    knight.protection = 0
    for arm in knight.armour:
        knight.protection += arm["protection"]

    # apply weapon
    knight.power += knight.weapon["power"]

    # apply potion if exist
    if knight.potion is not None:
        if "power" in knight.potion["effect"]:
            knight.power += knight.potion["effect"]["power"]

        if "protection" in knight.potion["effect"]:
            knight.protection += knight.potion["effect"]["protection"]

        if "hp" in knight.potion["effect"]:
            knight.hp += knight.potion["effect"]["hp"]

    return knight
