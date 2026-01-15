def fight(knight1: dict, knight2: dict) -> [int, int]:
    knight1_hp = knight1["hp"]
    knight2_hp = knight2["hp"]

    knight1_hp -= knight2["power"] - knight1["protection"]
    knight2_hp -= knight1["power"] - knight2["protection"]

    knight1_hp = max(0, knight1_hp)
    knight2_hp = max(0, knight2_hp)

    return knight1_hp, knight2_hp
