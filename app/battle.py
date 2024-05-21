from app.knights import Knight


def battle_result(knight1: Knight, knight2: Knight) -> None:
    knight1.hp = attack(knight1.hp, knight2.power, knight1.protection)
    knight2.hp = attack(knight2.hp, knight1.power, knight2.protection)


def attack(hp: int, power: int, protection: int) -> int:
    return is_hp_lt_zero(hp - (power - protection))


def is_hp_lt_zero(hp: int) -> int:
    return hp if hp > 0 else 0
