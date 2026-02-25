from app.models import Knight
from app.engine import conduct_duel


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }

    conduct_duel(knights["lancelot"], knights["mordred"])

    conduct_duel(knights["arthur"], knights["red_knight"])
    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
