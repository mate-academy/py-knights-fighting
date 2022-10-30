from app.knight import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"])
    arthur = Knight(knights["arthur"])
    mordred = Knight(knights["mordred"])
    red_knight = Knight(knights["red_knight"])

    lancelot.equip()
    arthur.equip()
    mordred.equip()
    red_knight.equip()

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
