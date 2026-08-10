from app.models.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    mordred = Knight(**knights_config["mordred"])
    arthur = Knight(**knights_config["arthur"])
    red_knight = Knight(**knights_config["red_knight"])

    lancelot.hp -= max(0, mordred.power - lancelot.protection)
    mordred.hp -= max(0, lancelot.power - mordred.protection)

    arthur.hp -= max(0, red_knight.power - arthur.protection)
    red_knight.hp -= max(0, arthur.power - red_knight.protection)

    lancelot.hp = max(0, lancelot.hp)
    mordred.hp = max(0, mordred.hp)
    arthur.hp = max(0, arthur.hp)
    red_knight.hp = max(0, red_knight.hp)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
