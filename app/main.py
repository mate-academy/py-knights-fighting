from app.knight import Knight
from app.knights_info import KNIGHTS


def battle(knights_config: dict) -> dict:
    list_of_instances = []
    for hero in knights_config:
        knight_instance = Knight(*knights_config[hero].values())
        knight_instance.preparations()
        list_of_instances.append(knight_instance)

    return (list_of_instances[0].battle_result(list_of_instances[2])
            | list_of_instances[1].battle_result(list_of_instances[3]))


print(battle(KNIGHTS))
