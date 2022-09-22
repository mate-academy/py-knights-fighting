from app.KHIGHTS_config import KNIGHTS
from app.apply_armour_weapon_potion import apply_armour_weapon_potion_if_exists
from app.battle import battle_function


def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = knightsConfig["lancelot"]
    lancelot = apply_armour_weapon_potion_if_exists(lancelot)

    # arthur
    arthur = knightsConfig["arthur"]
    arthur = apply_armour_weapon_potion_if_exists(arthur)

    # mordred
    mordred = knightsConfig["mordred"]
    mordred = apply_armour_weapon_potion_if_exists(mordred)

    # red_knight
    red_knight = knightsConfig["red_knight"]
    red_knight = apply_armour_weapon_potion_if_exists(red_knight)

    # BATTLE:
    # lancelot vs mordred
    # arthur vs red_knight

    return battle_function(lancelot, mordred, arthur, red_knight)


print(battle(KNIGHTS))
