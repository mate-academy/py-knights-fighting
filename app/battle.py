from app.knight import Knight


@staticmethod
def battle(knights: str) -> dict:
    lancelot = Knight(**knights["lancelot"])
    arthur = Knight(**knights["arthur"])
    mordred = Knight(**knights["mordred"])
    red_knight = Knight(**knights["red_knight"])

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
