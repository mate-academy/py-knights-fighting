from .knight import Knight


def apply_battle(knight_a: Knight, knight_b: Knight) -> None:

    damage_to_b: int = knight_a.power - knight_b.protection
    knight_b.hp -= damage_to_b

    damage_to_a: int = knight_b.power - knight_a.protection
    knight_a.hp -= damage_to_a

    knight_a.hp = max(knight_a.hp, 0)
    knight_b.hp = max(knight_b.hp, 0)
