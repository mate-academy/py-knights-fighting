from app.Players.Wariors import KNIGHTS
from app.actions.apply import apply_all_for
from app.actions.pvp import pvp

def battle(knightsConfig):
    # BATTLE PREPARATIONS:player [0], player [1], player [2], player [3]
    wariors_names_list = ["lancelot", "arthur", "mordred", "red_knight"]

    # make a warior list with objects "player"
    player_list = []
    for warior in wariors_names_list:
        player_list.append(knightsConfig[warior])

    # apply armour, weapon, potion if exist for everybody
    for player in player_list:
        apply_all_for(player)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    # check if someone fell in battle
    pvp(player_list[0], player_list[2])
    

    # 2 Arthur vs Red Knight:
    # check if someone fell in battle
    pvp(player_list[1], player_list[3])

    # Return battle results:
    return {player["name"]: player["hp"] for player in player_list}


print(battle(KNIGHTS))
