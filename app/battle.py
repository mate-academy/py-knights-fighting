from app.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.apply_equipment()

    lancelot.receive_damage(mordred.power)
    mordred.receive_damage(lancelot.power)

    arthur.receive_damage(red_knight.power)
    red_knight.receive_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
