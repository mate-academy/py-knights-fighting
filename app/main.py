from app.knights.class_knights import Knight
from app.knights.knights import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = {knight: Knight(knights_config[knight]["name"],
                              knights_config[knight]["power"],
                              knights_config[knight]["hp"],
                              knights_config[knight]["armour"],
                              knights_config[knight]["weapon"],
                              knights_config[knight]["potion"])
               for knight in knights_config}

    # BATTLE PREPARATIONS:
    for knight in knights.values():

        # apply armour
        knight.apply_armour()

        # apply weapon
        knight.apply_weapon()

        # apply potion if exist
        knight.apply_potion()

    # ------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights["lancelot"].battle(knights["mordred"])

    # 2 Arthur vs Red Knight:
    knights["arthur"].battle(knights["red_knight"])

    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }


print(battle(KNIGHTS))
