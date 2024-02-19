from app.battle_operations_module.battle import Battle
# from app.knight_data import KNIGHTS


def battle(base_knights_config: dict) -> dict:
    knights_list = [base_knights_config[key] for key in base_knights_config]
    for index in range(len(knights_list) - 2):
        participant_1 = knights_list[index]
        participant_2 = knights_list[index + 2]

        play_battle = Battle(
            fighter_one=participant_1,
            fighter_two=participant_2
        )

        play_battle.battle_begins()
    return Battle.result_of_all_battle
