from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot_attack = lancelot.power
    mordred_attack = mordred.power

    lancelot.take_damage(mordred_attack)
    mordred.take_damage(lancelot_attack)

    arthur_attack = arthur.power
    red_knight_attack = red_knight.power

    arthur.take_damage(red_knight_attack)
    red_knight.take_damage(arthur_attack)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
