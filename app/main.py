from .stats.potion_effect import potion_effect
from .stats.protection import protection
from .stats.weapon import weapon_add
from .battle.fight import fighting
from .battle.death_check import death_check
from .knights_dict import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knights_config['lancelot']

    # apply armour
    protection(lancelot)

    # apply weapon
    weapon_add(lancelot)

    # apply potion if exist
    potion_effect(lancelot)

    # arthur
    arthur = knights_config['arthur']

    # apply armour
    protection(arthur)

    # apply weapon
    weapon_add(arthur)

    # apply potion if exist
    potion_effect(arthur)

    # mordred
    mordred = knights_config['mordred']

    # apply armour
    protection(mordred)

    # apply weapon
    weapon_add(mordred)

    # apply potion if exist
    potion_effect(mordred)

    # red_knight
    red_knight = knights_config['red_knight']

    # apply armour
    protection(red_knight)

    # apply weapon
    weapon_add(red_knight)

    # apply potion if exist
    potion_effect(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fighting(lancelot, mordred)
    # check if someone fell in stats
    death_check(lancelot)
    death_check(mordred)

    # 2 Arthur vs Red Knight:
    fighting(arthur, red_knight)

    # check if someone fell in stats
    death_check(arthur)
    death_check(red_knight)

    # Return stats results:
    return {
        lancelot['name']: lancelot['hp'],
        arthur['name']: arthur['hp'],
        mordred['name']: mordred['hp'],
        red_knight['name']: red_knight['hp'],
    }


print(battle(KNIGHTS))
