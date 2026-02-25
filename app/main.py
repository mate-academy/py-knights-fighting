from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {k: Knight(**v) for k, v in knights_config.items()}
    for knight in knights.values():
        knight.prepare_for_battle()

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0
