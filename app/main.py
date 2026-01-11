from app.knight import Knight, fight
from app.config import KNIGHTS


def battle(knights_config: dict) -> dict:
    """
    Execute battles between knights and return results.

    Battles:
    - Lancelot vs Mordred
    - Arthur vs Red Knight
    """
    knights = {
        key: Knight.from_dict(config)
        for key, config in knights_config.items()
    }

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
