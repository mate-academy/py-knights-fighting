from app.knights.knight import Knight
from app.knights.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    list_of_instances = [
        Knight(
            name=knights_config[knight]["name"],
            hp=knights_config[knight]["hp"],
            power=knights_config[knight]["power"]
        )
        for knight in knights_config
    ]

    list_of_names = list(knights_config.keys())

    for index, knight in enumerate(list_of_instances):
        knight.get_additional(knights_config[list_of_names[index]])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot = list_of_instances[0]
    mordred = list_of_instances[2]
    lancelot - mordred
    mordred - lancelot

    # 2 Arthur vs Red Knight:
    arthur = list_of_instances[1]
    red_knight = list_of_instances[3]
    arthur - red_knight
    red_knight - arthur

    # Return battle results:
    return {
        lancelot.name: max(lancelot.hp, 0),
        arthur.name: max(arthur.hp, 0),
        mordred.name: max(mordred.hp, 0),
        red_knight.name: max(red_knight.hp, 0),
    }


print(battle(KNIGHTS))
