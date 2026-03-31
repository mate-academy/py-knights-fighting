from app.models.knight import Knight
from app.helpers.battle_logic import fight


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(config)
        for key, config in knights_config.items()
    }

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    fight(lancelot, mordred)
    fight(mordred, lancelot)

    fight(arthur, red_knight)
    fight(red_knight, arthur)

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
