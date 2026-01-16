from app.Knight import Knight


def duels(knight_list: list[Knight]) -> dict:
    result = {}
    knight_list[0].hp -= knight_list[2].power - knight_list[0].protection
    knight_list[2].hp -= knight_list[0].power - knight_list[2].protection
    knight_list[1].hp -= knight_list[3].power - knight_list[1].protection
    knight_list[3].hp -= knight_list[1].power - knight_list[3].protection
    for knight in knight_list:
        if knight.hp <= 0:
            knight.hp = 0
        result.update({knight.name: knight.hp})
    sorted_result = dict(sorted(result.items()))
    return sorted_result
