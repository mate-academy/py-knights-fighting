from app.battle_service import Battle
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(data)
        for key, data in knights_config.items()
    }

    Battle.fight(
        knights["lancelot"],
        knights["mordred"]
    )

    Battle.fight(
        knights["arthur"],
        knights["red_knight"]
    )

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
