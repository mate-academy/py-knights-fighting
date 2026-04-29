from app.knights import Knight


def battle_one(knight_one: Knight, knight_two: Knight) -> None:
    knight_one.hp = max(
        0,
        knight_one.hp - (knight_two.power - knight_one.protection)
    )
    knight_two.hp = max(
        0,
        knight_two.hp - (knight_one.power - knight_two.protection)
    )
