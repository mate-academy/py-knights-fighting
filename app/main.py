from app.knight_class import Knight
from app.knights_list import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(**stats)
        for name, stats in knights_config.items()
    }

    knights["lancelot"].battle(knights["mordred"])
    knights["arthur"].battle(knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
