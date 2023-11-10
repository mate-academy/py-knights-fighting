from app.preparation.class_knight import Knight


def pre_battle(knights: dict) -> Knight:
    lancelot = Knight(knights["lancelot"])
    lancelot.config()

    arthur = Knight(knights["arthur"])
    arthur.config()

    mordred = Knight(knights["mordred"])
    mordred.config()

    red_knight = Knight(knights["red_knight"])
    red_knight.config()

    return lancelot, arthur, mordred, red_knight
