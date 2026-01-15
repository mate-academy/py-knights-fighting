from app.battle_action import battle_act, battle_results
from app.battle_preparation import knight_preparation
from app.knights import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = knight_preparation.knight_option(knights_config["lancelot"])
    arthur = knight_preparation.knight_option(knights_config["arthur"])
    mordred = knight_preparation.knight_option(knights_config["mordred"])
    red_knight = knight_preparation.knight_option(knights_config["red_knight"])

    # BATTLE:
    lancelot_mordred = battle_act.battles(lancelot, mordred)
    arthur_red_knight = battle_act.battles(arthur, red_knight)

    # Return battle results:
    return battle_results.results(lancelot_mordred, arthur_red_knight)


print(battle(KNIGHTS))
