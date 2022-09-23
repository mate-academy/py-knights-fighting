from app.KHIGHTS_config import KNIGHTS
from app.apply_armour_weapon_potion import apply_armour_weapon_potion_if_exists
from app.battle import battle_function


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = knights_config["lancelot"]
    lancelot = apply_armour_weapon_potion_if_exists(lancelot)

    # arthur
    arthur = knights_config["arthur"]
    arthur = apply_armour_weapon_potion_if_exists(arthur)

    # mordred
    mordred = knights_config["mordred"]
    mordred = apply_armour_weapon_potion_if_exists(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]
    red_knight = apply_armour_weapon_potion_if_exists(red_knight)

    # BATTLE:
    # lancelot vs mordred
    # arthur vs red_knight

    return battle_function(lancelot, mordred, arthur, red_knight)


print(battle(KNIGHTS))
