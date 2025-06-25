from app.knights import KNIGHTS
from app.preparation import preparation
from app.battle import battle_round


def battle(knightsconfig: dict) -> dict[str, int]:
    list_knights = preparation(knightsconfig)
    result = battle_round(
        lancelot=list_knights[0],
        mordred=list_knights[2],
        arthur=list_knights[1],
        red_knight=list_knights[3]
    )
    return result


print(battle(KNIGHTS))
