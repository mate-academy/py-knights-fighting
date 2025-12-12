import random

from app.util.mappers import dict_list_to_knight_list


def get_knight_pairs(
        knights_dict: dict,
        random_pick: bool = False
) -> list[tuple]:
    knights_list = dict_list_to_knight_list(knights_dict)

    if random_pick:
        random.shuffle(knights_list)
        pairs = list(zip(knights_list[0::2], knights_list[1::2]))
        return pairs
    else:
        knight_names_dict = {
            "Lancelot": None,
            "Arthur": None,
            "Mordred": None,
            "Red Knight": None
        }

        for knight in knights_list:
            if knight.name in knight_names_dict:
                knight_names_dict[knight.name] = knight

        return [
            (
                knight_names_dict["Lancelot"],
                knight_names_dict["Mordred"]
            ), (
                knight_names_dict["Arthur"],
                knight_names_dict["Red Knight"]
            )
        ]
