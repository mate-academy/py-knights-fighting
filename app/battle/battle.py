from app.knights.knights import Knight


def do_battle(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    for knight in (knight1, knight2):
        if knight.hp < 0:
            knight.hp = 0


def battle_result(knights_dict: dict) -> dict:
    return {name : knight.hp for name, knight in knights_dict.items()}
