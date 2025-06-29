from app.knights import Knight


def strike(knight: Knight, opponent: Knight) -> None:
    damage = max(0, opponent.power - knight.protection)
    knight.hp = max(0, knight.hp - damage)


def fight(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.buff()
    knight_2.buff()
    strike(knight_1, knight_2)
    strike(knight_2, knight_1)
