from app.resourses import Knight


def battle(knightsConfig):
    lancelot = Knight(knightsConfig["lancelot"])
    arthur = Knight(knightsConfig["arthur"])
    mordred = Knight(knightsConfig["mordred"])
    red_knight = Knight(knightsConfig["red_knight"])

    for knight in (lancelot, arthur, mordred, red_knight):
        knight.prepare()

    lancelot.fight(mordred)
    mordred.fight(lancelot)

    arthur.fight(red_knight)
    red_knight.fight(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
