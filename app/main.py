from app.knights import KnightClass
from app.battle_module import Battle


def battle(knights_config):
    knight_dict = {}
    for knight in knights_config:
        kn = KnightClass(knights_config[knight])
        kn_dict = {knight: {
            "name": kn.name(),
            "protection": kn.protection(),
            "hp": kn.hp(),
            "power": kn.power()
        }}
        knight_dict.update(kn_dict)

    battle_pair = [(knight_dict["lancelot"], knight_dict["mordred"]),
                   (knight_dict["arthur"], knight_dict["red_knight"])]
    result = {}
    for pair in battle_pair:
        bt = Battle(pair)
        result.update(bt.result())

    return result
