from app.knight import Knight


def duel(knight1: Knight, knight2: Knight) -> None:
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)


def battle(knights_config: dict) -> None:
    knights = {k: Knight(v) for k, v in knights_config.items()}

    # prepare all knights
    for knight in knights.values():
        knight.prepare()

    # fights
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
