from app.knight import Knight
from app.knights_info import KNIGHTS


def battle(knights_config: dict) -> dict:
    for key in knights_config:
        knight_instance = Knight(knights_config[key]["name"],
                                 knights_config[key]["power"],
                                 knights_config[key]["hp"],
                                 knights_config[key]["armour"],
                                 knights_config[key]["weapon"],
                                 knights_config[key]["potion"])
        knight_instance.preparations()
        KNIGHTS[key] = knight_instance

    return KNIGHTS["lancelot"].battle_result(KNIGHTS["mordred"]) | \
        KNIGHTS["arthur"].battle_result(KNIGHTS["red_knight"])


print(battle(KNIGHTS))
