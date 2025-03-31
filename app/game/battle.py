def battle(knight1, knight2):
    knight1_damage = max(0, knight2.power - knight1.protection)
    knight2_damage = max(0, knight1.power - knight2.protection)

    knight1.hp = max(0, knight1.hp - knight1_damage)
    knight2.hp = max(0, knight2.hp - knight2_damage)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }