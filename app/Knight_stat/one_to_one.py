def one_to_one(knights: list[dict]) -> list[int]:
    fight = []
    fight.append(knights[0]["hp"] - knights[2]["power"])
    fight.append(knights[1]["hp"] - knights[3]["power"])
    fight.append(knights[2]["hp"] - knights[0]["power"])
    fight.append(knights[3]["hp"] - knights[1]["power"])
    for fighter in range(len(fight)):
        if fight[fighter] <= 0:
            fight[fighter] = 0
    return fight
