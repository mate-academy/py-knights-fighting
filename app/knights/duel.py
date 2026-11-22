from app.knights.knight import Knight


def duel(first: Knight, second: Knight) -> None:
    for attacker, defender in ((second, first), (first, second)):
        defender.hp -= attacker.power - defender.protection
        if defender.hp <= 0:
            defender.hp = 0
