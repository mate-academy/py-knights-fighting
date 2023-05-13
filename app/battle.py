from app.knights import Knight


def check_damage(hp: int, damage: int) -> int:
    if damage >= hp:
        return 0
    return hp - damage


def fight(knight_1: Knight, knight_2: Knight) -> None:
    damage_2 = knight_2.power - knight_1.protection
    damage_1 = knight_1.power - knight_2.protection
    knight_1.hp = check_damage(knight_1.hp, damage_2)
    knight_2.hp = check_damage(knight_2.hp, damage_1)
