from preparation.class_knight import Knight


def pre_battle(KNIGHTS: dict) -> Knight:
    lancelot = Knight(KNIGHTS["lancelot"])
    lancelot.config()

    arthur = Knight(KNIGHTS["arthur"])
    arthur.config()

    mordred = Knight(KNIGHTS["mordred"])
    mordred.config()

    red_knight = Knight(KNIGHTS["red_knight"])
    red_knight.config()

    return lancelot, arthur, mordred, red_knight
