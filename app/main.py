from app.person.knightsCLS import Knights
from app.DICT import KNIGHTS


def battle(knights_config: dict) -> dict:

    all_knights = Knights.from_dict(knights_config)

    lancelot = all_knights["lancelot"]
    mordred = all_knights["mordred"]

    arthur = all_knights["arthur"]
    red_knight = all_knights["red_knight"]

    result_1 = lancelot.fight(mordred)
    result_2 = arthur.fight(red_knight)

    final = {**result_1, **result_2}


    return final

