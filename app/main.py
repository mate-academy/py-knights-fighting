from app.config import KNIGHTS
from app.preparations import Knight
from app.battle import Battle


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(config)
        for name, config
        in knights_config.items()
    }

    Battle(knights["lancelot"], knights["mordred"])
    Battle(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


print(battle(KNIGHTS))
