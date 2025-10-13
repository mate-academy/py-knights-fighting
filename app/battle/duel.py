def duel(knight1: dict, knight2: dict) -> dict:
    damage_to_k2 = knight1.attack(knight2)
    damage_to_k1 = knight2.attack(knight1)

    knight1.take_damage(damage_to_k1)
    knight2.take_damage(damage_to_k2)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
