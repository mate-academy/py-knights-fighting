from app.battle.battle import battle_net, fight, return_results, clear_data
from app.knights.knight import Knight
from app.data.read_data import read_data_from_dict


def battle(knights_data: dict) -> dict:
    read_data_from_dict(knights_data)

    for couple in battle_net:
        fight(
            Knight.knights_arr[battle_net[couple][0]],
            Knight.knights_arr[battle_net[couple][1]]
        )

    result = return_results()
    clear_data()
    return result
