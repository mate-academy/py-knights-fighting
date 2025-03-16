from app.knights import KNIGHTS
from app.config import Knight


def create_knights(dict_of_knights: dict) -> tuple:
    lancelot = Knight(dict_of_knights.get("lancelot"))
    mordred = Knight(dict_of_knights.get("mordred"))
    arthur = Knight(dict_of_knights.get("arthur"))
    red_knight = Knight(dict_of_knights.get("red_knight"))
    return lancelot, mordred, arthur, red_knight


def battle(knight: dict) -> dict:
    lancelot, mordred, arthur, red_knight = create_knights(knight)

    lancelot.fight(mordred)
    mordred.fight(lancelot)
    arthur.fight(red_knight)
    red_knight.fight(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
