from app.data.read_data import ReadData
from app.battle.battle import Battle
from app.knights.knight import Knight


def battle(knights_data: dict) -> dict:
    ReadData.read_data_from_dict(knights_data)

    for couple in Battle.battle_net:
        Battle.fight(
            Knight.knights_arr[Battle.battle_net[couple][0]],
            Knight.knights_arr[Battle.battle_net[couple][1]]
        )

    return Battle.return_results()
