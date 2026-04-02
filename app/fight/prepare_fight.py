def prepare_table(knights: list) -> dict:
    result = {
        knights[i].display_name: 0
        for i in range(len(knights))
    }

    return result


def get_pairs(knights: list) -> list:
    pair1 = []
    pair2 = []
    for knight in knights:
        if (knight.display_name == "Lancelot"
                or knight.display_name == "Mordred"):
            pair1.append(knight)
        elif (knight.display_name == "Arthur"
              or knight.display_name == "Red Knight"):
            pair2.append(knight)

    return [pair1, pair2]
