from app.knight.knight import Knight


def apply_benefits(knight: Knight) -> None:
    apply_armour(knight)
    apply_weapon(knight)
    apply_potion(knight)


def apply_armour(knight: Knight) -> None:
    for armour in knight.armour:
        knight.protection += armour["protection"]


def apply_weapon(knight: Knight) -> None:
    knight.power += knight.weapon["power"]


def apply_potion(knight: Knight) -> None:
    if knight.potion is not None:
        for benefit, value in knight.potion["effect"].items():
            current_value = getattr(knight, benefit)
            setattr(knight, benefit, current_value + value)
