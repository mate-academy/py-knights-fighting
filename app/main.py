from app.kings import KNIGHTS
from app.stats.other_stats import armor, weapon
from app.stats.potion import apply_potion


def battle(knightsConfig: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knightsConfig["lancelot"]

    # apply armour
    lancelot = armor(lancelot)

    # apply weapon
    lancelot = weapon(lancelot)

    # apply potion if exist
    lancelot = apply_potion(lancelot)

    # arthur
    arthur = knightsConfig["arthur"]

    # apply armour
    arthur = armor(arthur)

    # apply weapon
    arthur = weapon(arthur)

    # apply potion if exist
    arthur = apply_potion(arthur)

    # mordred
    mordred = knightsConfig["mordred"]

    # apply armour
    mordred = armor(mordred)

    # apply weapon
    mordred = weapon(mordred)

    # apply potion if exist
    mordred = apply_potion(mordred)

    # red_knight
    red_knight = knightsConfig["red_knight"]

    # apply armour
    red_knight = armor(red_knight)

    # apply weapon
    red_knight = weapon(red_knight)

    # apply potion if exist
    red_knight = apply_potion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
