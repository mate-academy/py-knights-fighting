from app.knights.parameters import KNIGHTS
from app.knights.apply_all import apply_armor, apply_potion
from app.battle.fight import final_battle


def battle(knights_parameters: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knights_parameters["lancelot"]

    # apply armour
    lancelot["protection"] = apply_armor(lancelot)

    # apply weapon
    lancelot["power"] += lancelot["weapon"]["power"]

    # apply potion if exist
    apply_potion(lancelot)

    # arthur
    arthur = knights_parameters["arthur"]

    # apply armour
    arthur["protection"] = apply_armor(arthur)

    # apply weapon
    arthur["power"] += arthur["weapon"]["power"]

    # apply potion if exist
    apply_potion(arthur)

    # mordred
    mordred = knights_parameters["mordred"]

    # apply armour
    mordred["protection"] = apply_armor(mordred)

    # apply weapon
    mordred["power"] += mordred["weapon"]["power"]

    # apply potion if exist
    apply_potion(mordred)

    # red_knight
    red_knight = knights_parameters["red_knight"]

    # apply armour
    red_knight["protection"] = apply_armor(red_knight)

    # apply weapon
    red_knight["power"] += red_knight["weapon"]["power"]

    # apply potion if exist
    apply_potion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    final_battle(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    final_battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
