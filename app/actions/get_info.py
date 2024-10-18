from app.add_some_abilities.add_protection import protection
from app.add_some_abilities.add_power import power
from app.add_some_abilities.add_potion_abilities import add_ability_from_potion


def get_knights_info(knightscfg: dict) -> list:
    knights = []
    for knight in knightscfg:
        knights.append(knightscfg[knight])
        protection(knightscfg[knight])
        power(knightscfg[knight])
        if knightscfg[knight]["potion"] is not None:
            for eff in knightscfg[knight]["potion"]["effect"]:
                add_ability_from_potion(knightscfg[knight], eff)

    return knights
