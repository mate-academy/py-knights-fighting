def single_battle(*args) -> None:
    for knights in args:
        hp1 = knights[0]["hp"] - knights[1]["power"] + knights[0]["protection"]
        hp2 = knights[1]["hp"] - knights[0]["power"] + knights[1]["protection"]
        knights[0]["hp"], knights[1]["hp"] = hp1, hp2
        for i in range(2):
            if knights[i]["hp"] <= 0:
                knights[i]["hp"] = 0
