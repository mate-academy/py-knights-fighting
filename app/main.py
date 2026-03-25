from app.knight import Knight
from app.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(config) for key, config in knights_config.items()
    }

    knights["lancelot"].fight(knights["mordred"])
    knights["arthur"].fight(knights["red_knight"])

    return {
        knight.name: knight.hp for knight in knights.values()
    }


print(battle(KNIGHTS))
