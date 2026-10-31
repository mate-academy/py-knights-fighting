from app.knights import KNIGHTS
from app.apply_potion import apply_potion
from app.apply_armor_and_weapon import apply_armour
from app.apply_armor_and_weapon import apply_weapon


def battle(knights_config: KNIGHTS) -> None:

    # lancelot
    lancelot = knights_config["lancelot"]
    apply_armour(lancelot)
    apply_weapon(lancelot)
    apply_potion(lancelot)

    # arthur
    arthur = knights_config["arthur"]
    apply_armour(arthur)
    apply_weapon(arthur)
    apply_potion(arthur)

    # mordred
    mordred = knights_config["mordred"]
    apply_armour(mordred)
    apply_weapon(mordred)
    apply_potion(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]
    apply_armour(red_knight)
    apply_weapon(red_knight)
    apply_potion(red_knight)
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
