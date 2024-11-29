from app.knight import Knight


def is_healthy(knight: Knight) -> int:
    if knight.hp <= 0:
        knight.hp = 0
    return knight.hp


def one_pair_battle(knight1: Knight, knight2: Knight) -> dict:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    return {knight1.name: is_healthy(knight1),
            knight2.name: is_healthy(knight2)}


def final_battle(pairs: list) -> dict:
    total_scores = {}
    for pair in pairs:
        name1, name2 = pair
        knight1 = Knight.knights_instances[name1]
        knight2 = Knight.knights_instances[name2]
        total_scores.update(one_pair_battle(knight1, knight2))
    return total_scores
