from app.knight import Knight
from app.knight.config import get_knight_dict

KNIGHTS = get_knight_dict()


def battle(knights_dict: dict) -> dict:

    lancelot = Knight(knights_dict["lancelot"])
    arthur = Knight(knights_dict["arthur"])
    mordred = Knight(knights_dict["mordred"])
    red_knight = Knight(knights_dict["red_knight"])
    knights = [lancelot, arthur, mordred, red_knight]
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)

    # Return battle results:
    return {
        knight.name: knight.hp for knight in knights
    }


print(battle(KNIGHTS))
