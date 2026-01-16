from app.knights import Knight


def single_battle(knight1: Knight, knight2: Knight) -> dict:
    knight1.prepare_for_battle()
    knight2.prepare_for_battle()
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
