from fighting_config.character_param import KNIGHTS
import fighting_config.battle_class


def battle(knights_config: dict) -> dict:

    both_of_knights = (fighting_config.
                       battle_class.KnightsBattle(knights_config))
    # BATTLE PREPARATIONS:

    lancelot = both_of_knights.knights["lancelot"].show_info()
    arthur = both_of_knights.knights["arthur"].show_info()
    mordred = both_of_knights.knights["mordred"].show_info()
    red_knight = both_of_knights.knights["red_knight"].show_info()

    for knight in [lancelot, arthur, mordred, red_knight]:
        both_of_knights.parametrization_of_knight(knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    both_of_knights.knights_battle(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    both_of_knights.knights_battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
