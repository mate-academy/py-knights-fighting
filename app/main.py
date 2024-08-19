from app.knights_stats import knights
from app.battle_preparations import battle_preparations
from app.battle_result import result


def battle(dict_of_knights: dict) -> dict:
    lancelot, arthur, mordred, red_knight = (
        battle_preparations(dict_of_knights))

    result(lancelot, mordred)
    result(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(knights))
