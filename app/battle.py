from app.knight import Knight


def battle(knights_config: dict) -> dict:
    # CONFIG Knights objects
    knights = {
        name: Knight(**config) for name, config in knights_config.items()
    }

    for knight in knights.values():
        knight.apply_potion()

    # BATTLE:
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp for knight in knights.values()
    }


def duel(lancelot: Knight, mordred: Knight) -> None:
    lancelot.hp -= mordred.power - lancelot.armour.protection
    mordred.hp -= lancelot.power - mordred.armour.protection

    lancelot.hp = max(0, lancelot.hp)
    mordred.hp = max(0, mordred.hp)
