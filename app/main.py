from app.our_personages import KNIGHTS
from app.our_functions import put_on, is_alife, vs


def battle(knights_config: dict) -> dict:
    # lancelot
    lancelot = put_on(knights_config["lancelot"])
    # arthur
    arthur = put_on(knights_config["arthur"])
    # mordred
    mordred = put_on(knights_config["mordred"])
    # red_knight
    red_knight = put_on(knights_config["red_knight"])

    # 1 Lancelot vs Mordred:
    if is_alife(lancelot):
        lancelot = vs(lancelot, mordred)
    if is_alife(mordred):
        mordred = vs(mordred, lancelot)

    # 2 Arthur vs Red Knight:
    if is_alife(arthur):
        arthur = vs(arthur, red_knight)
    if is_alife(red_knight):
        red_knight = vs(red_knight, arthur)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
