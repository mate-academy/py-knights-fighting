from app.knights.calculation.count import stat
from app.knights.contest.count_bb import calculation_before_battle


def battle(main_dict: dict = None,
           first_pair: tuple = ("lancelot", "mordred"),
           second_pair: tuple = ("arthur", "red_knight")) -> dict:
    if main_dict is None:
        main_dict = {}
    result = {}
    result.update(calculation_before_battle(first_pair[0],
                                            first_pair[1], stat(main_dict)))
    result.update(calculation_before_battle(second_pair[0],
                                          second_pair[1], stat(main_dict)))
    base_dict = {"Lancelot": 0,
                 "Arthur": 0,
                 "Mordred": 0,
                 "Red Knight": 0}
    for key, value in result.items():
        base_dict[key] = value
    return base_dict
