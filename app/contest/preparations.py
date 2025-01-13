def apply_armor(knight) -> None:
    for armour_unit in knight.armour:
        knight.protection += armour_unit.get("protection")


def apply_weapon(knight) -> None:
    knight.power += knight.weapon.get("power")


def apply_potion(knight) -> None:
    if knight.potion is not None:
        if "power" in knight.potion["effect"]:
            knight.power += knight.potion["effect"]["power"]

        if "protection" in knight.potion["effect"]:
            knight.protection += knight.potion["effect"]["protection"]

        if "hp" in knight.potion["effect"]:
            knight.hp += knight.potion["effect"]["hp"]
