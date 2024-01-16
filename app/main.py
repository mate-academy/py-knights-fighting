from app.knight_class import Knight
from app.knights_default import KNIGHTS


def battle(knights_parameter: dict) -> dict:
    lancelot = Knight(knights_parameter["lancelot"])
    arthur = Knight(knights_parameter["arthur"])
    mordred = Knight(knights_parameter["mordred"])
    red_knight = Knight(knights_parameter["red_knight"])

    lancelot.fight(mordred)
    mordred.fight(lancelot)
    arthur.fight(red_knight)
    red_knight.fight(arthur)

    return Knight.return_result(lancelot, mordred, arthur, red_knight)


print(battle(KNIGHTS))
