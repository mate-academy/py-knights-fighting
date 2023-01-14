from app.knights import knights_stats
from app.knights import main_stats
from app.battles import first_battle
from app.battles import second_battle


def battle(knights_info):
    lancelot = main_stats.knight_stat(knights_info, knight_name="lancelot")
    arthur = main_stats.knight_stat(knights_info, knight_name="arthur")
    mordred = main_stats.knight_stat(knights_info, knight_name="mordred")
    red_knight = main_stats.knight_stat(knights_info, knight_name="red_knight")

    first_battle.lancelot_with_mordred(lancelot, mordred)
    second_battle.arthur_with_red_knight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(knights_stats.KNIGHTS))
