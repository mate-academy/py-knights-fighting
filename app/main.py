from app.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        knight: Knight(knights_config[knight])
        for knight in knights_config
    }

    Knight.battle(
        knights["lancelot"],
        knights["mordred"],
    )

    Knight.battle(
        knights["arthur"],
        knights["red_knight"],
    )

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
