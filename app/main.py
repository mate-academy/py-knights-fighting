from app.config import KNIGHTS
from app.battle.fight import fight, prepare_knights


def battle(knights_config: dict) -> dict:
    prepared_knights = prepare_knights(knights_config)

    return {
        **fight(
            prepared_knights["lancelot"],
            prepared_knights["mordred"],
        ),
        **fight(
            prepared_knights["arthur"],
            prepared_knights["red_knight"],
        ),
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
