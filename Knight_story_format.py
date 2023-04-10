if __name__ == "__main__":
    from app.event_items.event_master import Event
    from app.knight_items.knight_manipulation import (knight_dict_creation,
                                                      knight_fight,
                                                      tournament_result,
                                                      knight_obj_creation,
                                                      stats_calculation)
    from typing import Dict





    Event.ambience()
    Event.event_start()


    def battle(participants_dict: Dict[str, Dict]) -> Dict[str, int]:
        knight_obj_creation(participants_dict)
        stats_calculation()
        knight_fight("Lancelot", "Mordred")
        knight_fight("Artur", "Red Knight")
        return tournament_result()


    battle(knight_dict_creation())


