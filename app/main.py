from app.knight import Knight
from app.knight_config import knights


def battle(dict_of_knight: dict) -> dict:
    knights = Knight.battle_preparations(dict_of_knight)

    lancelot = next(knight for knight in knights if knight.name == "Lancelot")
    arthur = next(knight for knight in knights if knight.name == "Arthur")
    mordred = next(knight for knight in knights if knight.name == "Mordred")
    red_knight = next(knight
                      for knight
                      in knights
                      if knight.name == "Red Knight")

    Knight.result(lancelot, mordred)
    Knight.result(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knights))
