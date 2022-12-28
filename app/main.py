from app.dict_of_knights import KNIGHTS
from app.battle import battle_between_two_knights
from app.battle_preparations import battle_preparations


def battle(knights: dict) -> dict:
    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    battle_preparations(lancelot, arthur, mordred, red_knight)
    battle_between_two_knights(lancelot, mordred)
    battle_between_two_knights(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
