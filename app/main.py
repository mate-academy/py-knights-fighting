from app.config import KNIGHTS
from app.preparation import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }
    results = {}

    # BATTLE:
    # 1 Lancelot vs Mordred
    knights.get("lancelot").fight_vs(knights.get("mordred"))

    # 2 Arthur vs Red Knight
    knights.get("arthur").fight_vs(knights.get("red_knight"))

    # Check if someone fell in battle
    for knight in knights.values():
        results[knight.name] = knight.get_hp()

    return results


if __name__ == "__main__":
    print(battle(KNIGHTS))
