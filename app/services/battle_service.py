from app.models.knight import Knight


def fight(knight_1: Knight, knight_2: Knight) -> dict[str, int]:
    knight_1_damage = knight_2.total_power - knight_1.total_protection
    knight_2_damage = knight_1.total_power - knight_2.total_protection

    knight_1_hp = knight_1.total_hp - knight_1_damage
    knight_2_hp = knight_2.total_hp - knight_2_damage

    if knight_1_hp <= 0:
        knight_1_hp = 0

    if knight_2_hp <= 0:
        knight_2_hp = 0

    return {
        knight_1.name: knight_1_hp,
        knight_2.name: knight_2_hp,
    }
