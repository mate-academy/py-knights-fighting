from app.knights import KNIGHTS
from app.preparation import preparation
from app.battle import battle_round


def battle(knightsconfig: dict) -> dict[str, int]:
    list_knights = preparation(knightsconfig)
    result = battle_round(
        list_knights[0],
        list_knights[2],
        list_knights[1],
        list_knights[3]
    )
    return result


print(battle(KNIGHTS))
