from app.knight import Knight
from app.knights_data import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(**data) for key, data in knights_config.items()
    }

    knights["lancelot"].fight(knights["mordred"])
    knights["arthur"].fight(knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
