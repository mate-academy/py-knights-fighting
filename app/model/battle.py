from app.model.knight import Knight


def battle_between_knights(
        knight_a: Knight,
        knight_b: Knight
) -> None:
    damage_to_knight_a = knight_b.power - knight_a.protection
    damage_to_knight_b = knight_a.power - knight_b.protection

    knight_a.hp = max(0, knight_a.hp - damage_to_knight_a)
    knight_b.hp = max(0, knight_b.hp - damage_to_knight_b)
