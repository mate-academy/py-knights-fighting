def prepare_table(knights: list) -> dict:
    return {knight.display_name: 0 for knight in knights}


def get_pairs(knights: list) -> list:
    pair1 = []
    pair2 = []
    for knight in knights:
        if knight.display_name in ("Lancelot", "Mordred"):
            pair1.append(knight)
        elif knight.display_name in ("Arthur", "Red Knight"):
            pair2.append(knight)

    return [pair1, pair2]
