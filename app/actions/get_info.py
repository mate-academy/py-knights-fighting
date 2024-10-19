from app.add_some_abilities.add_protection import protection
from app.add_some_abilities.add_power import power
from app.add_some_abilities.add_potion_abilities import add_ability_from_potion


def get_knights_info(knightscfg: dict) -> list:
    knights = []
    for knight_name in knightscfg:
        knights.append(knightscfg[knight_name])
        protection(knightscfg[knight_name])
        power(knightscfg[knight_name])
        if knightscfg[knight_name]["potion"] is not None:
            for eff in knightscfg[knight_name]["potion"]["effect"]:
                add_ability_from_potion(knightscfg[knight_name], eff)

    return knights
