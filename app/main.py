from app.knight import Knight
from app.settings import KNIGHTS


def battle(knights_сonfig: dict) -> dict:

    lancelot = Knight(knights_сonfig["lancelot"])
    arthur = Knight(knights_сonfig["arthur"])
    mordred = Knight(knights_сonfig["mordred"])
    red_knight = Knight(knights_сonfig["red_knight"])

    knights = []
    knights.append(lancelot)
    knights.append(arthur)
    knights.append(mordred)
    knights.append(red_knight)
    for _ in knights:
        _.apply_gear()

    lancelot.duel(mordred)
    arthur.duel(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
