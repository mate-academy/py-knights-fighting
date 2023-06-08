from app.knight import Knight
from app.knights_info import KNIGHTS


def battle(knights_config: dict) -> dict:
    inst_dict = {}
    for hero in knights_config:
        knight_instance = Knight(*knights_config[hero].values())
        knight_instance.preparations()
        inst_dict[hero] = knight_instance

    return (inst_dict["lancelot"].battle_result(inst_dict["mordred"])
            | inst_dict["arthur"].battle_result(inst_dict["red_knight"]))


print(battle(KNIGHTS))
