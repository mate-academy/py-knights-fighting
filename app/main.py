from app.knights.class_knights import Knight
from app.knights.knights import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = {}
    for knight in knights_config:
        knight = Knight(knights_config[knight]["name"],
                        knights_config[knight]["power"],
                        knights_config[knight]["hp"],
                        knights_config[knight]["armour"],
                        knights_config[knight]["weapon"],
                        knights_config[knight]["potion"])
        knights[knight.name] = knight

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
    knights["Lancelot"].battle(knights["Mordred"])

    # 2 Arthur vs Red Knight:
    knights["Arthur"].battle(knights["Red Knight"])

    return {
        knights["Lancelot"].name: knights["Lancelot"].hp,
        knights["Arthur"].name: knights["Arthur"].hp,
        knights["Mordred"].name: knights["Mordred"].hp,
        knights["Red Knight"].name: knights["Red Knight"].hp,
    }


print(battle(KNIGHTS))
