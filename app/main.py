from event_master import event_start
from knights_creation import (
    Knight,
    knight_dict_creation,
    knight_obj_creation,
    knights_obj_list
    )

participants_dict = knight_dict_creation()
# print(participants_dict)
def battle(participants_dict):
    #Lancelot is battling versus Mordred and Arthur versus Red Knight
    knight_obj_creation(participants_dict)
    Knight.stats_calculation()

    print(knights_obj_list[0]["lancelot"].power)
    print(knights_obj_list[0]["arthur"].power)
    print(knights_obj_list[0]["mordred"].power)
    print(knights_obj_list[0]["red_knight"].power)
    # knights_obj_list[0]["Lancelot"].hp -= knights_obj_list[0]["Mordred"].power
    # knights_obj_list[0]["Mordred"].hp -= knights_obj_list[0]["Lancelot"].power
    # knights_obj_list[0]["Arthur"].hp -= knights_obj_list[0]["Red knight"].power
    # knights_obj_list[0]["Red knight"].hp -= knights_obj_list[0]["Arthur"].power

    #!!!!!!!(knights_obj_list[0]["Lancelot"].hp)



    # -------------------------------------------------------------------------------
#     # BATTLE:
#
#     # 1 Lancelot vs Mordred:
#     lancelot["hp"] -= mordred["power"] - lancelot["protection"]
#     mordred["hp"] -= lancelot["power"] - mordred["protection"]
#
#     # check if someone fell in battle
#     if lancelot["hp"] <= 0:
#         lancelot["hp"] = 0
#
#     if mordred["hp"] <= 0:
#         mordred["hp"] = 0
#
#     # 2 Arthur vs Red Knight:
#     arthur["hp"] -= red_knight["power"] - arthur["protection"]
#     red_knight["hp"] -= arthur["power"] - red_knight["protection"]
#
#     # check if someone fell in battle
#     if arthur["hp"] <= 0:
#         arthur["hp"] = 0
#
#     if red_knight["hp"] <= 0:
#         red_knight["hp"] = 0
#
#     # Return battle results:
#     return {
#         lancelot["name"]: lancelot["hp"],
#         arthur["name"]: arthur["hp"],
#         mordred["name"]: mordred["hp"],
#         red_knight["name"]: red_knight["hp"],
#     }
    return "RESULT"
print(battle(participants_dict))
