# from knight_manipulation import (Knight,
#                                  knight_dict_creation,
#                                  knight_fight,
#                                  tournament_result,
#                                  test_names, knights_obj_list)
from app.knight_manipulation import (Knight,
                                     knight_dict_creation,
                                     knight_fight,
                                     tournament_result,knights_obj_list)


def battle(participants_dict):
   #print(f"BASE_CONFING = {participants_dict}")

    Knight.knight_obj_creation(participants_dict)
    print("Before stat calc")
    print(f"{knights_obj_list[0].get('Lancelot').name} | HP:"
         f"{knights_obj_list[0].get('Lancelot').hp} | ATK: "
         f"{knights_obj_list[0].get('Lancelot').power}")
    Knight.stats_calculation()
    #print("______________________________")
    knight_fight("Lancelot", "Mordred")
    #print("______________________________")
    knight_fight("Artur", "Red Knight")
    #print("______________________________")
    return tournament_result()


battle(knight_dict_creation())