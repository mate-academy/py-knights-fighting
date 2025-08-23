from app.knights.knight import Knight


def fight(knight_1: Knight, knight_2: Knight) -> None:

    # Calcula o dano que cada cavaleiro sofre
    damage_to_knight_1 = max(0, knight_2.power - knight_1.protection)
    damage_to_knight_2 = max(0, knight_1.power - knight_2.protection)

    # Atualiza os pontos de vida
    knight_1.hp -= damage_to_knight_1
    knight_2.hp -= damage_to_knight_2

    # Garante que os pontos de vida não fiquem negativos
    knight_1.hp = max(0, knight_1.hp)
    knight_2.hp = max(0, knight_2.hp)
