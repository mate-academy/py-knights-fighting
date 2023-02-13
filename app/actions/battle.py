def action(rivals: dict, first: str, second: str) -> dict:
    # calculation of the knight's hp
    hp_first = rivals[second]["power"] - rivals[first]["protection"]
    rivals[first]["hp"] -= hp_first
    hp_second = rivals[first]["power"] - rivals[second]["protection"]
    rivals[second]["hp"] -= hp_second

    # check if someone fell in battle
    if rivals[first]["hp"] <= 0:
        rivals[first]["hp"] = 0

    if rivals[second]["hp"] <= 0:
        rivals[second]["hp"] = 0

    return rivals
