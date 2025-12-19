def fight(knight_1, knight_2) -> object:
    damage_to_1 = max(knight_2.power - knight_1.protection, 0)
    damage_to_2 = max(knight_1.power - knight_2.protection, 0)

    knight_1.take_damage(damage_to_1)
    knight_2.take_damage(damage_to_2)

    return {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp,
    }
