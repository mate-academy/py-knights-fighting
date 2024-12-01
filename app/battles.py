from app.knight import Knight


def one_pair_battle(knight1: Knight, knight2: Knight) -> dict:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    return {knight1.name: max(knight1.hp, 0),
            knight2.name: max(knight2.hp, 0)}


def final_battle(pairs: list) -> dict:
    total_scores = {}
    for pair in pairs:
        name1, name2 = pair
        knight1 = Knight.knights_instances[name1]
        knight2 = Knight.knights_instances[name2]
        total_scores.update(one_pair_battle(knight1, knight2))
    return total_scores
