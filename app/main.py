from knights.knight_preparation import Preparation
from actions.action import Action
from app.data import knights_info


def battle(knights_config: dict) -> dict:
    # init knights
    knights = []
    for knight in knights_config:
        knight = Preparation.init_knight(knight, knights_config)
        knights.append(knight)

    # equip knights
    for knight_name in range(len(knights_config)):
        Action.preparation(knights[knight_name])

    lancelot, arthur, mordred, red_knight = knights

    # battles
    Action.battle(lancelot, mordred)
    Action.battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knights_info))
