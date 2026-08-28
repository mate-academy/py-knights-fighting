from app.knight.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight_power = first_knight.power
    second_knight_power = second_knight.power

    first_knight.take_damage(second_knight_power)
    second_knight.take_damage(first_knight_power)


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
