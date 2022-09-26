from app.config import KNIGHTS
from app.apply_armour_weapon_potion import apply_armour_weapon_potion
from app.battle import battle_func


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = knights_config["lancelot"]
    lancelot = apply_armour_weapon_potion(lancelot)

    # arthur
    arthur = knights_config["arthur"]
    arthur = apply_armour_weapon_potion(arthur)

    # mordred
    mordred = knights_config["mordred"]
    mordred = apply_armour_weapon_potion(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]
    red_knight = apply_armour_weapon_potion(red_knight)

    # BATTLE:
    # lancelot vs mordred
    # arthur vs red_knight

    return battle_func(lancelot, mordred, arthur, red_knight)


print(battle(KNIGHTS))
