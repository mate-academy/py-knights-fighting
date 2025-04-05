from app.knight.knight import Knight


def prepare(knight: Knight) -> None:
    knight.power += knight.weapon.get_power()

    knight.protection = knight.armour.total_protection()

    if knight.potion:
        for stat, value in knight.potion.get_effect().items():
            if stat == "hp":
                knight.hp += value
            elif stat == "power":
                knight.power += value
            elif stat == "protection":
                knight.protection += value

    knight.hp = max(0, knight.hp)
    knight.power = max(0, knight.power)
    knight.protection = max(0, knight.protection)
