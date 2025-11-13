from .stats.potion_effect import potion_effect
from .stats.protection import protection
from .stats.weapon import weapon_add
from .battle.fight import fighting
from .battle.death_check import death_check
from .knights_dict import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    for knight in knights_config.values():
        protection(knight)
        weapon_add(knight)
        potion_effect(knight)

    # Pary do walki
    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    # Przeprowadzenie walk w pętli
    for knight1_name, knight2_name in battles:
        knight1 = knights_config[knight1_name]
        knight2 = knights_config[knight2_name]

        fighting(knight1, knight2)
        death_check(knight1)
        death_check(knight2)

    # Return stats results:
    return {knight["name"]: knight["hp"] for knight in knights_config.values()}


print(battle(KNIGHTS))
