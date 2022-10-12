from app.knight import Knight


def battle(knights_config: dict) -> dict:

    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot.battle_preparation()
    arthur.battle_preparation()
    mordred.battle_preparation()
    red_knight.battle_preparation()

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    lancelot.hp = max(lancelot.hp, 0)
    mordred.hp = max(mordred.hp, 0)

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    arthur.hp = max(arthur.hp, 0)
    red_knight.hp = max(red_knight.hp, 0)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
