from app.for_act.knights import KNIGHTS
from app.for_act.battle_and_defeat import battles
from app.for_act.preparation import prepare_to_the_battle


def battle(knights: dict) -> dict:
    ready_knight = []
    for name in knights:
        knight = knights[name]
        prepare_to_the_battle(knight)
        ready_knight.append(knight)
    knight_d = {i + 1: knight for i, knight in enumerate(ready_knight)}
    battles([knight_d[1], knight_d[3]], [knight_d[2], knight_d[4]])
    return {knight_d[i]["name"]: knight_d[i]["hp"] for i in knight_d}


print(battle(KNIGHTS))
