from app.apply.all import apply_all
from app.battle.fight import fight
from app.battle.check_hp import check_hp


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    lancelot = knights_config["lancelot"]
    apply_all(lancelot)

    arthur = knights_config["arthur"]
    apply_all(arthur)

    mordred = knights_config["mordred"]
    apply_all(mordred)

    red_knight = knights_config["red_knight"]
    apply_all(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # check if someone fell in battle
    check_hp(lancelot)
    check_hp(mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # check if someone fell in battle
    check_hp(arthur)
    check_hp(red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
