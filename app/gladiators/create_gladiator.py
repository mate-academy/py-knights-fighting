from app.gladiators.gladiator_object import Gladiator


def create_gladiator(knights: dict) -> dict:
    dict_knights = {}
    for knight in knights:
        dict_knights[knight] = (Gladiator(knights[knight]["name"],
                                          knights[knight]["power"],
                                          knights[knight]["hp"],
                                          knights[knight]["armour"],
                                          knights[knight]["weapon"],
                                          knights[knight]["potion"]))
    return dict_knights
