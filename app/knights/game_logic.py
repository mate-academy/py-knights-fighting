from app.knights.models import Knight


def calculate_damage(attacker: Knight, defender: Knight) -> int:
    return attacker.power - defender.protection


def battle_round(knight_1: Knight, knight_2: Knight) -> None:
    dmg_to_1 = calculate_damage(attacker=knight_2, defender=knight_1)
    dmg_to_2 = calculate_damage(attacker=knight_1, defender=knight_2)

    knight_1.take_damage(dmg_to_1)
    knight_2.take_damage(dmg_to_2)
