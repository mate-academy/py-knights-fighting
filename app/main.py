from app.knights import KNIGHTS
from app.weapon_and_armour.apply_armour import ApplyArmour
from app.weapon_and_armour.apply_weapon import ApplyWeapon
from app.weapon_and_armour.apply_potion import ApplyPotion
from app.battle.check_fell import CheckFell
from app.battle.fight import Fight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knights_config["lancelot"]

    # apply armour
    ApplyArmour(lancelot)

    # apply weapon
    ApplyWeapon(lancelot)

    # apply potion if exist
    ApplyPotion(lancelot)
    # arthur
    arthur = knights_config["arthur"]

    # apply armour
    ApplyArmour(arthur)

    # apply weapon
    ApplyWeapon(arthur)

    # apply potion if exist
    ApplyPotion(arthur)

    # mordred
    mordred = knights_config["mordred"]

    # apply armour
    ApplyArmour(mordred)

    # apply weapon
    ApplyWeapon(mordred)

    # apply potion if exist
    ApplyPotion(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]

    # apply armour
    ApplyArmour(red_knight)

    # apply weapon
    ApplyWeapon(red_knight)

    # apply potion if exist
    ApplyPotion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Fight(lancelot, mordred)
    Fight(mordred, lancelot)

    # check if someone fell in battle
    CheckFell(lancelot)

    CheckFell(mordred)

    # 2 Arthur vs Red Knight:
    Fight(arthur, red_knight)
    Fight(red_knight, arthur)

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


if __name__ == "__main__":
    print(battle(KNIGHTS))
