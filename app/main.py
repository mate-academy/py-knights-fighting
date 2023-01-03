from app.for_act.knights import KNIGHTS
from app.for_act.defeat import defeat_check
from app.for_act.preparation import prepare_to_the_battle


def battle(knights_config: dict) -> dict:

    knight_list = []
    for name in knights_config:
        knight = knights_config[name]
        prepare_to_the_battle(knight)
        knight_list.append(name)

    knight_d = {i + 1: knights_config[knight_list[i]] for i in range(4)}

    knight_d[1]["hp"] -= knight_d[3]["power"] - knight_d[1]["protection"]
    knight_d[3]["hp"] -= knight_d[1]["power"] - knight_d[3]["protection"]
    knight_d[2]["hp"] -= knight_d[4]["power"] - knight_d[2]["protection"]
    knight_d[4]["hp"] -= knight_d[2]["power"] - knight_d[4]["protection"]

    defeat_check([knight_d[1], knight_d[2], knight_d[3], knight_d[4]])

    return {
        knight_d[1]["name"]: knight_d[1]["hp"],
        knight_d[2]["name"]: knight_d[2]["hp"],
        knight_d[3]["name"]: knight_d[3]["hp"],
        knight_d[4]["name"]: knight_d[4]["hp"],
    }


print(battle(KNIGHTS))
