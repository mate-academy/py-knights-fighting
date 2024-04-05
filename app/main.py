from app.battle.ready_to_battle import ready_to_battle
from app.battle.fight import fighting


def battle(knightsconfig: dict) -> dict:
    knight_list = ready_to_battle(knightsconfig)
    return {
        knight_list[0][0]: fighting(knight_list[0], knight_list[2]),
        knight_list[1][0]: fighting(knight_list[1], knight_list[3]),
        knight_list[2][0]: fighting(knight_list[2], knight_list[0]),
        knight_list[3][0]: fighting(knight_list[3], knight_list[1])
    }
