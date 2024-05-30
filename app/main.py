from app.character.knight_dict import KNIGHTS
from app.character.knight import Knight
from app.character.duel import duel


def battle(knights: dict[dict]) -> dict:
    lancelot, arthur, mordred, red_knight = Knight.knight_preparation(knights)
    result1 = duel(lancelot, mordred)
    result2 = duel(arthur, red_knight)
    return {**result1, **result2}


print(battle(KNIGHTS))
