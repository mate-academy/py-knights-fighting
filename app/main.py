from app.hero.knight import Knights


def battle(KNIGHTS):
    lancelot = Knights.create_knight(KNIGHTS["lancelot"])
    arthur = Knights.create_knight(KNIGHTS["arthur"])
    mordred = Knights.create_knight(KNIGHTS["mordred"])
    red_knight = Knights.create_knight(KNIGHTS["red_knight"])

    lancelot.fight(mordred)

    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
