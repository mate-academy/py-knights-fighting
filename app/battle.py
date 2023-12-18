from app.knight import Knights
# from app.knightsConfig import KNIGHTS


def battle(knight: dict) -> dict:
    lancelot = Knights(knight["lancelot"])
    arthur = Knights(knight["arthur"])
    mordred = Knights(knight["mordred"])
    red_knight = Knights(knight["red_knight"])

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
