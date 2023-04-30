from app.Knight_stat.calc_knight_stat import knight_stat
from app.Knight_stat.one_to_one import one_to_one


def battle(knights_main: dict) -> dict:

    knights = []
    for knight in knights_main.values():
        knights.append(knight_stat(knight))
    return {knights_main[knight]["name"]: one_to_one(knights)[number]
            for number, knight in enumerate(knights_main)}
