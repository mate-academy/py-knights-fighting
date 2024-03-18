from app.knight import Knight


knights_dict = {}


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:
    for knight_key, knight_info in knights.items():
        knight_inst = Knight(
            knight_info.get("name"),
            knight_info.get("power"),
            knight_info.get("hp")
        )
        knight_inst.apply_armour(knight_info.get("armour"))

        knight_inst.apply_weapon(knight_info.get("weapon"))

        knight_potion = knight_info.get("potion")
        if knight_potion is not None:
            knight_inst.apply_potion(knight_potion)

        knights_dict[knight_key] = knight_inst
    # -------------------------------------------------------------------------------
    # BATTLE:
    knights_dict["lancelot"].battle(knights_dict["mordred"])
    knights_dict["arthur"].battle(knights_dict["red_knight"])

    return {knight.name: knight.hp for knight in knights_dict.values()}
