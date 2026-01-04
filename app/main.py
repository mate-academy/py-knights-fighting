from app.primary_received_info import KNIGHTS
from app.class_and_their_description import KnightCreator


def battle(knights_config: dict) -> dict:
    list_of_knights_with_upgrade: [name for name in knights_config] = (
        [
            KnightCreator(knights_config.get(key)).
            upgrading_knight_before_battle(knights_config.get(key))
            for key in knights_config
        ]
    )

    first_round = KnightCreator.battle_rules(
        list_of_knights_with_upgrade[0],
        list_of_knights_with_upgrade[2]
    )

    second_round = KnightCreator.battle_rules(
        list_of_knights_with_upgrade[1],
        list_of_knights_with_upgrade[3]
    )

    first_round.update(second_round)

    return first_round


print(battle(KNIGHTS))
