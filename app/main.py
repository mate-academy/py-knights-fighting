from app.consts.knights import KNIGHTS
from app.bin.randomisation.mix import change_begin_data  # noqa: F401
from app.bin.classes import Knight


def battle(knights_config: dict) -> dict:
    cur_battle_knights = {}
    for name_key, knight in knights_config.items():
        cur_battle_knights[name_key] = Knight(knight)
    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    cur_battle_knights["lancelot"].fight(cur_battle_knights["mordred"])
    # 2 Arthur vs Red Knight:
    cur_battle_knights["arthur"].fight(cur_battle_knights["red_knight"])
    return {
        cur_battle_knights["lancelot"].name:
            cur_battle_knights["lancelot"].hp,
        cur_battle_knights["arthur"].name:
            cur_battle_knights["arthur"].hp,
        cur_battle_knights["mordred"].name:
            cur_battle_knights["mordred"].hp,
        cur_battle_knights["red_knight"].name:
            cur_battle_knights["red_knight"].hp
    }


print(battle(KNIGHTS))
