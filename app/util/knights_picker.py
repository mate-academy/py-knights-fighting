import random

from app.util.mappers import dict_list_to_knight_list


def get_knight_pairs(knights_dict: dict, random_pick: bool = False) -> [tuple]:
    knights_list = dict_list_to_knight_list(knights_dict)

    if random_pick:
        random.shuffle(knights_list)
        pairs = list(zip(knights_list[0::2], knights_list[1::2]))
        return pairs
    else:
        lancelot = next(
            knight
            for knight in knights_list if knight.name == "Lancelot"
        )
        arthur = next(
            knight
            for knight in knights_list if knight.name == "Arthur"
        )
        mordred = next(
            knight
            for knight in knights_list if knight.name == "Mordred"
        )
        red_knight = next(
            knight
            for knight in knights_list if knight.name == "Red Knight"
        )
        return [(lancelot, mordred), (arthur, red_knight)]
