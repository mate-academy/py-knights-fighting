from app.knight import Knight


def battle_preparations(knights_dict: dict) -> list:
    lancelot, arthur, mordred, red_knight = [
        Knight(**knights_dict[knight]) for knight in knights_dict]

    for knight in [lancelot, arthur, mordred, red_knight]:
        Knight.battle_preparations(knight)

    return [lancelot, arthur, mordred, red_knight]
