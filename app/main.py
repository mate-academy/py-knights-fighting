from app.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(config)
        for key, config in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare_for_battle()

    knights["lancelot"].fight(knights["mordred"])
    knights["arthur"].fight(knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
