from app.knight.one_knight import Knight


def potion_preparation(knight: Knight) -> Knight:
    if knight.potion is not None:
        knight.power += knight.potion["effect"].get("power", 0)
        knight.hp += knight.potion["effect"].get("hp", 0)
        knight.protection += knight.potion["effect"].get("protection", 0)
        return knight
    return knight
