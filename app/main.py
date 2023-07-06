from app.modules.knights import Knight


def fight(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection

    # check if someone fell in battle
    if knight_1.hp <= 0:
        knight_1.hp = 0

    if knight_2.hp <= 0:
        knight_2.hp = 0


def battle(knights_config: dict) -> dict | str:
    # knights = {knight["name"]: Knight(knight) for knight in knights_config}
    knights = {}

    for knight, value in knights_config.items():
        knights[knight] = Knight(value)

    # LET THE BATTLE BEGIN
    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
