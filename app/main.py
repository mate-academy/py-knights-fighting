from app.knight import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"])
    mordred = Knight(knights["mordred"])
    arthur = Knight(knights["arthur"])
    red_knight = Knight(knights["red_knight"])

    lancelot.fight_with(mordred)
    arthur.fight_with(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
