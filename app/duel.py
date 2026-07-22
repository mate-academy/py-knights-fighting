from app.knights import Knight


def duel(knight_a: Knight, knight_b: Knight) -> None:
    knight_a.hp = max(0, knight_a.hp - (knight_b.power - knight_a.protection))
    knight_b.hp = max(0, knight_b.hp - (knight_a.power - knight_b.protection))
