from app.knight import Knight
from app.data import KNIGHTS


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:
    dict_knights = {k: Knight(v) for k, v in knights.items()}

    #  4 Objects Knights
    lancelot = dict_knights["lancelot"]
    red_knight = dict_knights["red_knight"]
    arthur = dict_knights["arthur"]
    mordred = dict_knights["mordred"]

    # BATTLE:

    # 1 Lancelot vs Mordred:

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # 2 Arthur vs Red Knight:
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # check if someone fell in battle

    for knight in dict_knights.values():
        if knight.hp <= 0:
            knight.hp = 0

    # Return battle results:
    return {k.name: k.hp for k in dict_knights.values()}


print(battle(KNIGHTS))
