from app.models.knight import Knight


def increase_protection(knight: Knight) -> None:
    if knight.armours:
        for armour in knight.armours.armours:
            knight.protection += armour.protection
    if knight.potion:
        knight.protection += knight.potion.effect.protection


def increase_power(knight: Knight) -> None:
    knight.power += knight.weapon.power
    if knight.potion:
        knight.power += knight.potion.effect.power


def increase_health(knight: Knight) -> None:
    if knight.potion:
        knight.hp += knight.potion.effect.hp


def knight_prepared(knight: Knight) -> None:
    increase_protection(knight)
    increase_power(knight)
    increase_health(knight)
