from app.knights import KNIGHTS
from app.weapon_and_armour.apply_armour import ApplyArmour
from app.weapon_and_armour.apply_weapon import ApplyWeapon
from app.weapon_and_armour.apply_potion import ApplyPotion
from app.battle_vs.check_fell import CheckFell
from app.battle_vs.vs import VS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knights_config["lancelot"]

    # apply armour
    ApplyArmour(lancelot)

    # apply weapon_and_armour
    ApplyWeapon(lancelot)

    # apply potion if exist
    ApplyPotion(lancelot)

    # arthur
    arthur = knights_config["arthur"]

    # apply armour
    ApplyArmour(arthur)

    # apply weapon_and_armour
    ApplyWeapon(arthur)

    # apply potion if exist
    ApplyPotion(arthur)

    # mordred
    mordred = knights_config["mordred"]

    # apply armour
    ApplyArmour(mordred)

    # apply weapon_and_armour
    ApplyWeapon(mordred)

    # apply potion if exist
    ApplyPotion(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]

    # apply armour
    ApplyArmour(red_knight)

    # apply weapon_and_armour
    ApplyWeapon(red_knight)

    # apply potion if exist
    ApplyPotion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    VS(lancelot, mordred)
    VS(mordred, lancelot)

    # check if someone fell in battle
    CheckFell(lancelot)

    CheckFell(mordred)

    # 2 Arthur vs Red Knight:
    VS(arthur, red_knight)
    VS(red_knight, arthur)

    # check if someone fell in battle
    CheckFell(arthur)

    CheckFell(red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
