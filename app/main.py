from knights.knight_preparation import Preparation
from actions.action import Action
from app.data import knights_info


def battle(knights_config: dict) -> dict:
    # init knights
    lancelot = Preparation.init_knight("lancelot", knights_config)
    arthur = Preparation.init_knight("arthur", knights_config)
    mordred = Preparation.init_knight("mordred", knights_config)
    red_knight = Preparation.init_knight("red_knight", knights_config)

    # equip knights
    Action.preparation(lancelot)
    Action.preparation(arthur)
    Action.preparation(mordred)
    Action.preparation(red_knight)

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
