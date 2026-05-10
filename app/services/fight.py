from app.models.models import Knight


def duel(duel_pair: list[Knight]) -> dict:
    sorted_list_pairs = duel_pair[0::2] + duel_pair[1::2]

    result_fight = {}
    while sorted_list_pairs:
        knight_1 = sorted_list_pairs[0]
        knight_2 = sorted_list_pairs[1]
        knight_2.hp -= max(0, knight_1.power - knight_2.protection)
        knight_1.hp -= max(0, knight_2.power - knight_1.protection)
        if knight_2.hp <= 0:
            knight_2.hp = 0
        if knight_1.hp <= 0:
            knight_1.hp = 0
        result_fight[knight_1.name] = knight_1.hp
        result_fight[knight_2.name] = knight_2.hp
        sorted_list_pairs.remove(knight_1)
        sorted_list_pairs.remove(knight_2)
    return result_fight
