from app.battle import Battle
from app.knight.factory import get_knights
from app.config import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = get_knights(knights_config)

    first_battle = Battle()
    result1 = first_battle.fight(knights[0], knights[2])

    second_battle = Battle()
    result2 = second_battle.fight(knights[1], knights[3])

    return {**result1, **result2}


if __name__ == "__main__":
    battle(KNIGHTS)
