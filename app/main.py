from app.data import KNIGHTS
from app.knight import Knight
from app.duel import duel


def battle(knight_config: dict) -> dict:
    lancelot = Knight(knight_config["lancelot"])
    arthur = Knight(knight_config["arthur"])
    mordred = Knight(knight_config["mordred"])
    red_knight = Knight(knight_config["red_knight"])

    battle1 = duel(lancelot, mordred)
    battle2 = duel(arthur, red_knight)

    return {**battle1, **battle2}


if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
