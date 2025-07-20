def duel(knight1, knight2):
    k1_damage = max(knight2.power - knight1.protection, 0)
    k2_damage = max(knight1.power - knight2.protection, 0)

    knight1.hp = max(knight1.hp - k1_damage, 0)
    knight2.hp = max(knight2.hp - k2_damage, 0)

    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
