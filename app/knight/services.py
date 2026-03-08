from app.knight.models import Knight


def apply_armour(knight: Knight) -> None:
    knight.protection = sum(a.protection for a in knight.armour)


def apply_weapon(knight: Knight) -> None:
    if knight.weapon:
        knight.power += knight.weapon.power


def apply_potion(knight: Knight) -> None:
    if knight.potion:
        effect = knight.potion.effect
        knight.hp += effect.get("hp", 0)
        knight.power += effect.get("power", 0)
        knight.protection += effect.get("protection", 0)


def prepare_knight(knight: Knight) -> None:
    knight.hp = knight.base_hp
    knight.power = knight.base_power
    knight.protection = 0

    apply_armour(knight)
    apply_weapon(knight)
    apply_potion(knight)

    knight.protection = max(0, knight.protection)
