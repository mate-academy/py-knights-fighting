from app.knight.knight import Knight


def apply_buffs(knights: list[Knight]) -> None:

    for knight in knights:
        knight.protection = 0

        for armour_el in knight.armour:
            knight.protection += armour_el.protection

        knight.power += knight.weapon.power

        if knight.potion is not None:

            if "power" in knight.potion.effect:
                knight.power += knight.potion.effect["power"]
            if "hp" in knight.potion.effect:
                knight.hp += knight.potion.effect["hp"]
            if "protection" in knight.potion.effect:
                knight.protection += knight.potion.effect["protection"]
