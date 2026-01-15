from app.consts.knights import KNIGHTS
from app.bin.randomisation.mix import change_begin_data  # noqa: F401
from app.bin.classes import Knight


def battle(knights_config: dict) -> dict:
    curent_battle_knights = {}
    for name_key, knight in knights_config.items():
        curent_battle_knights[name_key] = Knight(knight)
    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    curent_battle_knights["lancelot"].fight(curent_battle_knights["mordred"])
    # 2 Arthur vs Red Knight:
    curent_battle_knights["arthur"].fight(curent_battle_knights["red_knight"])
    return {curent_battle_knights[knight].name:
            curent_battle_knights[knight].hp
            for knight in curent_battle_knights.keys()}


print(battle(KNIGHTS))
