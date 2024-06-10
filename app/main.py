from app.knight import Knight
from app.settings import KNIGHTS


def battle(knights_сonfig: dict) -> dict:
    lancelot = Knight(knights_сonfig["lancelot"])
    lancelot.apply_gear()

    arthur = Knight(knights_сonfig["arthur"])
    arthur.apply_gear()

    mordred = Knight(knights_сonfig["mordred"])
    mordred.apply_gear()

    red_knight = Knight(knights_сonfig["red_knight"])
    red_knight.apply_gear()

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
