from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare_for_battle()

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot.fight(mordred)
    mordred.fight(lancelot)

    arthur.fight(red_knight)
    red_knight.fight(arthur)

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
