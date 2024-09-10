from app.knight import Knight
from app.knigts_config import KNIGHTS


def battle(knights: dict) -> dict:
    lancelot, arthur, mordred, red_knight = (
        Knight.create_knight(knight)
        for knight in knights.values()
    )
    knights = (lancelot, arthur, mordred, red_knight)

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {knight.name: knight.hp for knight in knights}


if __name__ == "__main__":
    print(battle(KNIGHTS))
