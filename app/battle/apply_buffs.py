from app.knights.data import Knight
# This func calculate knight stats when equipment is applied


def stats(knight: Knight) -> None:
    # apply weapon
    knight.power += knight.weapon.get("power")
    # apply armour
    for part in knight.armour:
        knight.protection += part.get("protection")
    # apply potion if exist
    if knight.potion is not None:
        if "power" in knight.potion["effect"]:
            knight.power += knight.potion["effect"]["power"]
        if "protection" in knight.potion["effect"]:
            knight.protection += knight.potion["effect"]["protection"]
        if "hp" in knight.potion["effect"]:
            knight.hp += knight.potion["effect"]["hp"]
