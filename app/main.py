from app.knight.configure_stats import (get_config,
                                        apply_armor,
                                        apply_weapon,
                                        apply_potion,
                                        KNIGHTS)
from app.knight.fight import fight

knights = KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = get_config(knights_config, "lancelot")

    # apply armour
    apply_armor(lancelot)

    # apply weapon
    apply_weapon(lancelot)

    # apply potion if exist
    apply_potion(lancelot)

    # arthur
    arthur = get_config(knights_config, "arthur")

    # apply armour
    apply_armor(arthur)

    # apply weapon
    apply_weapon(arthur)

    # apply potion if exist
    apply_potion(arthur)

    # mordred
    mordred = get_config(knights_config, "mordred")

    # apply armour
    apply_armor(mordred)

    # apply weapon
    apply_weapon(mordred)

    # apply potion if exist
    apply_potion(mordred)

    # red_knight
    red_knight = get_config(knights_config, "red_knight")

    # apply armour
    apply_armor(red_knight)

    # apply weapon
    apply_weapon(red_knight)

    # apply potion if exist
    apply_potion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
