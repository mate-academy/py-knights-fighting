from app.battle.battle import fight
from app.knights.config import KNIGHTS
from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight.from_config(config)
        for key, config in knights_config.items()
    }

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
