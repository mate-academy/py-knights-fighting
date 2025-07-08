from app.KNIGHTS.knights import Knight


def battle(knights_config: dict) -> dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    # Lancelot vs Mordred battle
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # Arthur vs Red Knight battle
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
