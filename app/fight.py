def get_fight_result(knights: list) -> dict:

    result = {
        knights[i].display_name: 0
        for i in range(len(knights))
    }  # create a table for participants

    for i in range((len(knights) // 2)):  # each pair make fight

        knights[i].hp -= knights[i + 2].power - knights[i].protection
        knights[i + 2].hp -= knights[i].power - knights[i + 2].protection

        if knights[i].hp > 0:
            result[knights[i].display_name] = knights[i].hp

        if knights[i + 2].hp > 0:
            result[knights[i + 2].display_name] = knights[i + 2].hp

    return result
