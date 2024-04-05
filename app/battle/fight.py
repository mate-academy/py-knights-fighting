def fighting(knight1: tuple, knight2: tuple) -> int:
    knight1_hp = knight1[1] - (knight2[3] - knight1[2])
    if knight1_hp <= 0:
        knight1_hp = 0
    return knight1_hp
