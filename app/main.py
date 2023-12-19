from participants.change_participant import apply
from participants.battle import after_battle
from participants.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = apply(knights_config["lancelot"])

    arthur = apply(knights_config["arthur"])

    mordred = apply(knights_config["mordred"])

    red_knight = apply(knights_config["red_knight"])

    lancelot = after_battle(lancelot, mordred)
    mordred = after_battle(mordred, lancelot)

    arthur = after_battle(arthur, red_knight)
    red_knight = after_battle(red_knight, arthur)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
