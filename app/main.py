from app.knights_stats import KNIGHTS
from app.knights.knight import Knight


def battle(knight_config: dict) -> dict:
    knights = [Knight.from_dict(knight) for knight in knight_config.values()]
    lancelot, arthur, mordred, red_knight = knights

    Knight.fight(lancelot, mordred)
    Knight.fight(arthur, red_knight)

    return {knight.name: knight.hp for knight in knights}


if __name__ == "__main__":
    print(battle(KNIGHTS))
