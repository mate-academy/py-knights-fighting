if __name__ == "__main__":
    from event_master import Event
    from knight_manipulation import (knight_dict_creation,
                                     knight_fight,
                                     tournament_result, knight_obj_creation,
                                     stats_calculation)
else:
    from app.knight_manipulation import (Knight, knight_fight,stats_calculation,
                                         knight_dict_creation,knight_obj_creation,
                                         tournament_result)
    from app.event_master import Event




Event.ambience()
Event.event_start()

def battle(participants_dict):
    knight_obj_creation(participants_dict)
    stats_calculation()
    knight_fight("Lancelot", "Mordred")
    knight_fight("Artur", "Red Knight")

    return tournament_result()
battle(knight_dict_creation())

