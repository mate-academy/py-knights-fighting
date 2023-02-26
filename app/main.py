from app.knight_data import Knight
from app.knights import knight_data


def battle(knight: dict) -> dict:
    lancelot = Knight(knight["lancelot"])
    lancelot.added()
    mordred = Knight(knight["mordred"])
    mordred.added()
    arthur = Knight(knight["arthur"])
    arthur.added()
    red_knight = Knight(knight["red_knight"])
    red_knight.added()
    lancelot.duel(mordred)
    arthur.duel(red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knight_data))
