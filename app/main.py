from app.knights_config import knights
from app.battle_preparations import battle_preparations
from app.battle_results import result


def battle(dict_of_knight: dict) -> dict:
    lancelot, arthur, mordred, red_knight = battle_preparations(dict_of_knight)
    result(lancelot, mordred)
    result(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knights))
