from app.knights_processing.knights_making import Knight


def gearing(knight: Knight) -> None:
    for armour_piece in knight.armour:
        knight.protection += armour_piece["protection"]
    knight.power += knight.weapon["power"]
    if knight.potion is not None:
        if knight.potion["effect"].get("power"):
            knight.power += knight.potion["effect"]["power"]
        if knight.potion["effect"].get("protection"):
            knight.protection += knight.potion["effect"]["protection"]
        if knight.potion["effect"].get("hp"):
            knight.hp += knight.potion["effect"]["hp"]
