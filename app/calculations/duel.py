from app.knights.prepared_knight import PreparedKnight


def duel(knight_one: PreparedKnight, knight_two: PreparedKnight) -> dict:
    damage_to_one = max(0, knight_two.power - knight_one.protection)
    damage_to_two = max(0, knight_one.power - knight_two.protection)

    knight_one.hp -= damage_to_one
    knight_two.hp -= damage_to_two

    knight_one.hp = max(0, knight_one.hp)
    knight_two.hp = max(0, knight_two.hp)

    return {knight_one.name: knight_one.hp, knight_two.name: knight_two.hp}
