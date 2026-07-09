from app.battle import fight
from app.config import KNIGHTS
from app.knight import Knight


def create_knights(
    knights_config: dict,
) -> dict:
    return {
        name: Knight(config)
        for name, config in knights_config.items()
    }


def battle(knights_config: dict) -> dict:
    knights = create_knights(knights_config)

    fight(
        knights["lancelot"],
        knights["mordred"],
    )

    fight(
        knights["arthur"],
        knights["red_knight"],
    )

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
