from app.knight import Knight


def battle_preparations(knight_dict: dict) -> list:
    lancelot, arthur, mordred, red_knight = [
        Knight(**knight_dict[knight]) for knight in knight_dict]

    for knight in [lancelot, arthur, mordred, red_knight]:
        Knight.get_ready_to_battle(knight)

    return [lancelot, arthur, mordred, red_knight]
