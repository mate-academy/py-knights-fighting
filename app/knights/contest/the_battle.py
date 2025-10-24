from app.knights.calculation.count import calculate_all_stats
from app.knights.contest.count_bb import simulate_battle


def battle(main_dict: dict,
           first_pair: tuple = ("lancelot", "mordred"),
           second_pair: tuple = ("arthur", "red_knight")) -> dict:
    if main_dict is None:
        main_dict = {}
    result = {}
    stats_result = calculate_all_stats(main_dict)
    result.update(simulate_battle(first_pair[0],
                                  first_pair[1], stats_result))
    result.update(simulate_battle(second_pair[0],
                                  second_pair[1], stats_result))
    base_dict = {"Lancelot": 0,
                 "Arthur": 0,
                 "Mordred": 0,
                 "Red Knight": 0}
    for key, value in result.items():
        base_dict[key] = value
    return base_dict
