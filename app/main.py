from app.Knight import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"])
    mordred = Knight(knights["mordred"])
    arthur = Knight(knights["arthur"])
    red_knight = Knight(knights["red_knight"])

    knights_list = [lancelot, mordred, arthur, red_knight]

    for knight in knights_list:
        knight.prepare_for_battle()

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
