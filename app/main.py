from app.knights import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"])
    mordred = Knight(knights["mordred"])
    arthur = Knight(knights["arthur"])
    red_knight = Knight(knights["red_knight"])
    lancelot.fight(mordred)
    arthur.fight(red_knight)
    return knights_stats(lancelot, arthur, mordred, red_knight)


def knights_stats(*knights) -> dict:
    return {knight.name: knight.hp for knight in knights}
