from app.data.knights import KNIGHTS
from app.modules.knight import Knight


def battle(knights_config: dict):

    # PREPARE KNIGHTS DATA:
    participants = create_participants_list(knights_config)


def create_participants_list(knights_data: dict) -> dict:
    for name in knights_data:
        knight = Knight(*knights_data[name].values())
        knights_data[name] = knight
    return knights_data


print(battle(KNIGHTS))
