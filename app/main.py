from app.config import KNIGHTS
from app.knights.knight import Knight


BATTLE_PAIRS = (
    ("lancelot", "mordred"),
    ("arthur", "red_knight"),
)


def battle(knights_config: dict) -> dict[str, int]:
    # BATTLE PREPARATIONS:
    knights = {
        knight_name: Knight.from_config(config)
        for knight_name, config in knights_config.items()
    }

    # BATTLE:
    for first_knight, second_knight in BATTLE_PAIRS:
        knights[first_knight].take_damage(knights[second_knight])
        knights[second_knight].take_damage(knights[first_knight])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }

if __name__ == "__main__":
    print(battle(KNIGHTS))
