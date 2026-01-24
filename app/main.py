from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    # -------------------------------------------------------------------------------
    # BATTLE:
    knights_dict = {}
    for knight_name, knight in knights_config.items():
        knights_dict[knight_name] = Knight(
            knight["power"],
            knight["hp"],
            knight["armour"],
            knight["weapon"],
            knight["potion"]
        )
    # 1 Lancelot vs Mordred:
    knights_dict["lancelot"].battle_vs(knights_dict["mordred"])
    knights_dict["mordred"].battle_vs(knights_dict["lancelot"])

    knights_dict["arthur"].battle_vs(knights_dict["red_knight"])
    knights_dict["red_knight"].battle_vs(knights_dict["arthur"])

    result_dict = {}
    for knight_name, knight in knights_dict.items():
        if "_" in knight_name:
            new_knight_name = knight_name.replace("_", " ")
            result_dict[new_knight_name.title()] = knight.hp
        else:
            result_dict[knight_name.capitalize()] = knight.hp

    # Return battle results:
    return result_dict
