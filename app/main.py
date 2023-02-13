from app.knights_list import Knights
from app.actions.preparations import battle_preparations
from app.actions.battle import action


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    new_knights = battle_preparations(knights_config)

    # BATTLE:

    # 1 Lancelot vs Mordred:
    action(new_knights, "lancelot", "mordred")

    # 2 Arthur vs Red Knight:
    action(new_knights, "arthur", "red_knight")

    # Return battle results:
    return {
        new_knights["lancelot"]["name"]: new_knights["lancelot"]["hp"],
        new_knights["arthur"]["name"]: new_knights["arthur"]["hp"],
        new_knights["mordred"]["name"]: new_knights["mordred"]["hp"],
        new_knights["red_knight"]["name"]: new_knights["red_knight"]["hp"],
    }


print(battle(Knights.features))
