from app.knights import knights_stats
from app.knights import knights_check
from app.battles import first_battle
from app.battles import second_battle


def battle(knights_config):
    lancelot = knights_check.knights_check(knights_config, knight_name="lancelot")
    arthur = knights_check.knights_check(knights_config, knight_name="arthur")
    mordred = knights_check.knights_check(knights_config, knight_name="mordred")
    red_knight = knights_check.knights_check(knights_config, knight_name="red_knight")

    first_battle.lancelot_with_mordred(lancelot, mordred)
    second_battle.arthur_with_red_knight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(knights_stats.KNIGHTS))
