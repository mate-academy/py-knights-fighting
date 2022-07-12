def battle(battle_list):
    knight1 = battle_list[0]
    knight2 = battle_list[1]
    result1 = knight1.hp - (knight2.power - knight1.protection)
    result2 = knight2.hp - (knight1.power - knight2.protection)
    return {knight1.name: (result1 if result1 > 0 else 0),
            knight2.name: (result2 if result2 > 0 else 0)}
