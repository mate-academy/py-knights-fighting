from app.knight import KNIGHTS
from app.battle import battles
from app.characteristics import armour, weapon, potion


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knightsConfig["lancelot"]
    armour.apply_armour(lancelot)
    weapon.amply_weapon(lancelot)
    potion.amply_potion(lancelot)

    # arthur
    arthur = knightsConfig["arthur"]
    armour.apply_armour(arthur)
    weapon.amply_weapon(arthur)
    potion.amply_potion(arthur)

    # mordred
    mordred = knightsConfig["mordred"]
    armour.apply_armour(mordred)
    weapon.amply_weapon(mordred)
    potion.amply_potion(mordred)

    # red_knight
    red_knight = knightsConfig["red_knight"]
    armour.apply_armour(red_knight)
    weapon.amply_weapon(red_knight)
    potion.amply_potion(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battl_1 = battles(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    battl_2 = battles(arthur, red_knight)

    battl_1.update(battl_2)

    # Return battle results:
    return battl_1


print(battle(KNIGHTS))
