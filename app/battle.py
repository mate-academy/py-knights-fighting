from app.knight import Knight


def battle(knight: dict) -> dict:
    lancelot = Knight(knight["lancelot"])
    arthur = Knight(knight["arthur"])
    mordred = Knight(knight["mordred"])
    red_knight = Knight(knight["red_knight"])

    lancelot.preparation()
    arthur.preparation()
    mordred.preparation()
    red_knight.preparation()

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
