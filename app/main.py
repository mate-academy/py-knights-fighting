from app.knight import Knight
from app.knights_config import knights


def battle(dict_of_knight: dict) -> dict:
    fighter = Knight.battle_preparations(dict_of_knight)

    lancelot = fighter["lancelot"]
    arthur = fighter["arthur"]
    mordred = fighter["mordred"]
    red_knight = fighter["red_knight"]

    Knight.result(lancelot, mordred)
    Knight.result(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(knights))
