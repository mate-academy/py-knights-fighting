from app.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    lancelot.preparation_to_battle()
    mordred.preparation_to_battle()

    lancelot.battle(mordred)

    lancelot.check_is_fall()
    mordred.check_is_fall()

    arthur.preparation_to_battle()
    red_knight.preparation_to_battle()

    arthur.battle(red_knight)

    arthur.check_is_fall()
    red_knight.check_is_fall()

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
