import copy

from app.knights_data import KNIGHTS


def get_knights() -> dict:
    return copy.deepcopy(KNIGHTS)
