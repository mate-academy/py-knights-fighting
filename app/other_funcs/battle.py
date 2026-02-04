def battle_func(knights: dict) -> dict:
    knights_list = list(knights.keys())

    for i in range(len(knights_list) // 2):
        knights[knights_list[i]].battle(knights[knights_list[i + 2]])
        knights[knights_list[i + 2]].battle(knights[knights_list[i]])
    return knights
