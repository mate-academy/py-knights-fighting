from app.knights.knights_info import KNIGHTS
from app.battles.arthur_red_knight_battle import arthur_red_knight_battle
from app.battles.lancelot_mordred_battle import lancelot_mordred_battle
from app.knights.battle_preparations import prepare


def battle(knights_config: dict) -> dict:
    lancelot = prepare(knights_config, "lancelot")
    mordred = prepare(knights_config, "mordred")
    arthur = prepare(knights_config, "arthur")
    red_knight = prepare(knights_config, "red_knight")

    arthur_red_knight_battle(arthur, red_knight)
    lancelot_mordred_battle(lancelot, mordred)

    print("--------------------------------")
    print("And results of battles are:")

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"]
    }


print(battle(KNIGHTS))
