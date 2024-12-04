from app.knight_config import KNIGHTS
from app.battle import battle_between_two_knights, battle_results
from app.preparations.create_knights import create_dict_of_knights


def battle(knights_configuration: dict) -> dict:
    knights_dict = create_dict_of_knights(knights_configuration)
    battle_list = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for battles in battle_list:
        battle_between_two_knights(
            knights_dict[battles[0]],
            knights_dict[battles[1]]
        )

    return battle_results(knights_dict)


print(battle(KNIGHTS))
