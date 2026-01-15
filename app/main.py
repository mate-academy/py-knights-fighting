from app.knight_class import Knight
from app.stats import knights


def battle(knights_parameter: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knights_parameter["lancelot"])

    # arthur
    arthur = Knight(knights_parameter["arthur"])

    # mordred
    mordred = Knight(knights_parameter["mordred"])

    # red_knight
    red_knight = Knight(knights_parameter["red_knight"])
    # -------------------------------------------------------------------------------
    # BATTLE:
    lancelot.take_damage(mordred)
    mordred.take_damage(lancelot)
    arthur.take_damage(red_knight)
    red_knight.take_damage(arthur)

    # Return battle results:
    return Knight.return_result(lancelot, mordred, arthur, red_knight)


print(battle(knights))
