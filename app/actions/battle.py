def action(rivals: dict, first: str, second: str) -> dict:
    # calculation of the knight's hp
    first_rival = rivals.get(first)
    second_rival = rivals.get(second)

    hp_first = second_rival.get("power") - first_rival.get("protection")
    hp_second = first_rival.get("power") - second_rival.get("protection")

    first_rival.update(hp=first_rival.get("hp") - hp_first)
    second_rival.update(hp=second_rival.get("hp") - hp_second)

    # check if someone fell in battle
    if rivals[first]["hp"] < 0:
        rivals[first]["hp"] = 0

    if rivals[second]["hp"] < 0:
        rivals[second]["hp"] = 0

    return rivals
