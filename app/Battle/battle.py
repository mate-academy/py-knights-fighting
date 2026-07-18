from app.Knight_config.knight_config import prepare_to_battle


def battle(dict_with_knights: dict) -> dict:
    prepared_knight = prepare_to_battle(dict_with_knights)

    prepared_knight[0].hp -= (prepared_knight[2].power
                              - prepared_knight[0].protection)
    prepared_knight[2].hp -= (prepared_knight[0].power
                              - prepared_knight[2].protection)
    prepared_knight[1].hp -= (prepared_knight[3].power
                              - prepared_knight[1].protection)
    prepared_knight[3].hp -= (prepared_knight[1].power
                              - prepared_knight[3].protection)
    result_dict = {}
    for knight in prepared_knight:
        if knight.hp <= 0:
            knight.hp = 0
        result_dict[knight.name] = knight.hp
    return result_dict
