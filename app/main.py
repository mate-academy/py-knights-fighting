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

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
