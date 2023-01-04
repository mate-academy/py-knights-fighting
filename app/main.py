from app.for_act.knights import KNIGHTS
from app.for_act.battle_and_defeat import single_battle
from app.for_act.preparation import prepare_to_the_battle


def battle(knights: dict) -> dict:
    knight_ls = []
    for name in knights:
        knight = knights[name]
        prepare_to_the_battle(knight)
        knight_ls.append(name)
    knight_d = {i + 1: knights[knight_ls[i]] for i in range(4)}
    single_battle([knight_d[1], knight_d[3]], [knight_d[2], knight_d[4]])
    return {knight_d[i]["name"]: knight_d[i]["hp"] for i in range(1, 5)}


print(battle(KNIGHTS))
