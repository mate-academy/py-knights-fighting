def battle(knight1, knight2) -> dict:
    knight1.receive_damage(knight2.power)
    knight2.receive_damage(knight1.power)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }
