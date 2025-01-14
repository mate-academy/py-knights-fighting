from typing import Dict


def create_potion(name: str, effect: Dict[str, int]) \
        -> Dict[str, Dict[str, int]]:
    """
    Create a potion with a given name and effects.

    :param name: The name of the potion.
    :param effect: A dictionary of effects the potion applies.
    :return: A dictionary representing the potion.
    """
    return {"name": name, "effect": effect}
