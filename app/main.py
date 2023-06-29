from app.players.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot, arthur, mordred, red_knight = (
        Knight.from_dict(knight) for knight in knights_config.values()
    )
    lancelot.battles(mordred)
    arthur.battles(red_knight)
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
