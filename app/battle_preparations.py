from app.knight import Knight


def battle_preparations(knights_dict: dict) -> list:
    lancelot, arthur, mordred, red_knight = [
        Knight(name=knights_dict[knight]["name"],
               power=knights_dict[knight]["power"],
               hp=knights_dict[knight]["hp"],
               armour=knights_dict[knight]["armour"],
               weapon=knights_dict[knight]["weapon"],
               potion=knights_dict[knight]["potion"]
               ) for knight in knights_dict.keys()]

    for knight in [lancelot, arthur, mordred, red_knight]:
        Knight.battle_preparations(knight)

    return [lancelot, arthur, mordred, red_knight]
