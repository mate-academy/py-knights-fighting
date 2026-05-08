from app.utils.constants import KNIGHTS
from app.knights.knight_config import Knight


def battle(
        knights_conf: dict
) -> dict:
    knights_battle = Knight(knights_conf)
    battle_ = knights_battle.battle()
    return battle_


if __name__ == "__main__":
    battle_n = battle(KNIGHTS)
