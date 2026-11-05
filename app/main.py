from app.stats.other_stats import armor, weapon
from app.stats.potion import apply_potion
from app.battle import hit


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    for king in knights_config.values():
        armor(king)
        weapon(king)
        apply_potion(king)

    # lancelot
    lancelot = knights_config["lancelot"]

    # arthur
    arthur = knights_config["arthur"]

    # mordred
    mordred = knights_config["mordred"]

    # red_knight
    red_knight = knights_config["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    hit(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    hit(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
