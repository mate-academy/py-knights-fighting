from app.battle_begin.logic_battle import Logic
from knights import KNIGHTS
from app.before_battle.basic_states import New_Knight
from app.before_battle.calculate_states import Calculate


print(KNIGHTS)


def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    knights = {}
    for key, value in knightsConfig.items():
        knights[value['name']] = New_Knight(
            value['name'],
            value['power'],
            value['hp'])
        level_up = Calculate(value['armour'],
                            value['weapon'],
                            value['potion'])

        knights[value['name']].improve_states(level_up)
    print('level up : ', knights['Mordred'].hp)

    logic = Logic()
    logic.ready_set_go(knights)



    # New_Knight.additional_states(knight)
battle(KNIGHTS)


#     # -------------------------------------------------------------------------------
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
#
#
# print(battle(KNIGHTS))
