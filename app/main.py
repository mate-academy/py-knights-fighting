from knight_manipulation import (Knight,
                                 knight_dict_creation,
                                 knight_fight,
                                 tournament_result, knight_obj_creation)
from event_master import event_start

# from app.knight_manipulation import (Knight, knight_obj_creation,
#                                      knight_dict_creation,
#                                      knight_fight,
#                                      tournament_result)
# from app.event_master import event_start


def battle(participants_dict):
    event_start()
    knight_obj_creation(participants_dict)
    Knight.stats_calculation()
    knight_fight("Lancelot", "Mordred")
    knight_fight("Artur", "Red Knight")
    return tournament_result()


battle(knight_dict_creation())
