from app.data.knights import KNIGHTS
from app.data.tournament import tournament
from app.modules.knight import Knight


def battle(knights_config: dict) -> dict:

    # PREPARE KNIGHTS DATA:
    participants = create_participants_list(knights_config)

    # CARRY OUT BATTLES
    for opponents in tournament:
        left, right = opponents
        if left in participants and right in participants:
            fight(participants[left], participants[right])

    # RETURN KNIGHTS HP INFO AFTER THE TOURNAMENT
    return {knight.name: knight.hp for knight in participants.values()}


def create_participants_list(knights_data: dict) -> dict:
    for name in knights_data:
        knight = Knight(*knights_data[name].values())
        knights_data[name] = knight
    return knights_data


def fight(left_knight: Knight, right_knight: Knight) -> None:
    left_knight.fighting(right_knight)
    right_knight.fighting(left_knight)


print(battle(KNIGHTS))
