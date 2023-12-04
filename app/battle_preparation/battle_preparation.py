from app.knights.knight import Knight


def knights_power_calculation(knight: Knight) -> Knight:
    if hasattr(knight, "weapon"):
        knight.power += knight.weapon.power
    if hasattr(knight, "armour"):
        knight.protection = 0
        knight.protection += sum(unit.protection for unit in knight.armour)
    if hasattr(knight, "potion"):
        if "power" in knight.potion.effect:
            knight.power += knight.potion.effect["power"]
        if "protection" in knight.potion.effect:
            knight.protection += knight.potion.effect["protection"]
        if "hp" in knight.potion.effect:
            knight.hp += knight.potion.effect["hp"]
    return knight
