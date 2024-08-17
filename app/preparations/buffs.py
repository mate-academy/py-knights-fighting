from app.knight.knight import Knight


def apply_buffs(knights: list[Knight]) -> None:

    for knight in knights:

        knight.protection = sum(
            armour_element.protection for armour_element in knight.armour
        )

        knight.power += knight.weapon.power

        if knight.potion is not None:

            if "power" in knight.potion.effect:
                knight.power += knight.potion.effect.get("power")
            if "hp" in knight.potion.effect:
                knight.hp += knight.potion.effect.get("hp")
            if "protection" in knight.potion.effect:
                knight.protection += knight.potion.effect.get("protection")
