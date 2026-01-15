from app.knights.param import Knight
from app.battle.knights_battle import knights_battle


def battle(knights_config: dict) -> dict:

    # BATTLE PREPARATIONS:
    name_list = ["lancelot", "arthur", "mordred", "red_knight"]
    knights_dict = {}
    for barbar in name_list:
        knights_dict[barbar] = Knight(
            knights_config[barbar]["name"],
            knights_config[barbar]["hp"],
            knights_config[barbar]["power"]
        )
    for name, value in knights_dict.items():
        value.calculate_param(knights_config[name])

    # -------------------------------------------------------------------------------
    # BATTLE:

    knights_battle(knights_dict["lancelot"], knights_dict["mordred"])
    knights_battle(knights_dict["arthur"], knights_dict["red_knight"])

    # Return battle results:
    return {knight.name: knight.hp for knight in knights_dict.values()}
