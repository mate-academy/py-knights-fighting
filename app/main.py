from app.classes.knight_class import Knight


def battle(knights):
    dc_of_knights = Knight.from_dict_to_class(knights)

    # FIRST BATTLE
    dc_of_knights['lancelot'].battle_knights(dc_of_knights['mordred'])

    # SECOND BATTLE
    dc_of_knights['arthur'].battle_knights(dc_of_knights['red_knight'])

    return {dc_of_knights[knight].name: dc_of_knights[knight].hp
            for knight in dc_of_knights}
