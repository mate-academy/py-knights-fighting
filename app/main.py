from app.character.knight_dict import KNIGHTS
from app.character.knight import Knight
from app.character.battle import battle


def main(knights: dict[dict]) -> dict:
    lancelot, arthur, mordred, red_knight = Knight.knight_preparation(knights)
    result1 = battle(lancelot, mordred)
    result2 = battle(arthur, red_knight)
    return {**result1, **result2}


print(main(KNIGHTS))
