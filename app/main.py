from app.combat import fight
from app.config import KNIGHTS
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        identifier: Knight(configuration)
        for identifier, configuration in knights_config.items()
    }
    for first, second in (("lancelot", "mordred"), ("arthur", "red_knight")):
        fight(knights[first], knights[second])
    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
