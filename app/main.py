from app.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(**knights_config[name])
        for name, config in knights_config.items()
    }
    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    lancelot.execute_duel(mordred)
    arthur.execute_duel(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
