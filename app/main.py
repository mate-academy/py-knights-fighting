from app.knight_items.knight_manipulation import (for_pytest_func,
                                                  knight_dict_creation)


from typing import Dict


def battle(participants_dict: Dict[str, Dict]) -> Dict[str, int]:
    return for_pytest_func(participants_dict)


battle(knight_dict_creation())
