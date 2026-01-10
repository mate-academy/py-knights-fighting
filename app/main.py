from app.knight import Knight


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:
    dict_knights = {k: Knight(v) for k, v in knights.items()}

    #  4 Objects Knights
    lancelot = dict_knights["lancelot"]
    red_knight = dict_knights["red_knight"]
    arthur = dict_knights["arthur"]
    mordred = dict_knights["mordred"]

    # BATTLE:

    battle_pairs = [(lancelot, mordred), (arthur, red_knight)]
    for pair in battle_pairs:
        pair[0].take_damage(pair[1].power)
        pair[1].take_damage(pair[0].power)

    # Return battle results:
    return {k.name: k.hp for k in dict_knights.values()}
