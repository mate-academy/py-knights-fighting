from knight_manipulation import (Knight, knight_dict_creation,
                                 knight_fight,tournament_result)


def battle(participants_dict):
    Knight.knight_obj_creation(participants_dict)
    Knight.stats_calculation()
    knight_fight("Lancelot", "Mordred")
    knight_fight("Arthur", "Red Knight")
    return tournament_result()


print(battle(knight_dict_creation()))
