from app.knights import KNIGHTS
from app.knight_stats import knight_stats
from app.duel import duel
# importing refactored functions and dictionary


def battle(knights_dict):
    # getting stats from other file using function and dictionary
    lancelot = knight_stats(knights_dict["lancelot"])
    mordred = knight_stats(knights_dict["mordred"])
    arthur = knight_stats(knights_dict["arthur"])
    red_knight = knight_stats(knights_dict["red_knight"])
    # BATTLE:
    duel(lancelot, mordred)
    duel(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
