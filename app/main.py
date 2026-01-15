from app.Kingdom_of_Camelot.knights import KNIGHTS
from app.knights_duel.duel_arena import DuelArena


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    lancelot = DuelArena.ready_up(knights_config["lancelot"])
    arthur = DuelArena.ready_up(knights_config["arthur"])
    mordred = DuelArena.ready_up(knights_config["mordred"])
    red_knight = DuelArena.ready_up(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot["hp"] = DuelArena.battle_knights(
        first_knight=lancelot,
        second_knight=mordred
    )
    mordred["hp"] = DuelArena.battle_knights(
        first_knight=mordred,
        second_knight=lancelot
    )

    # 2 Arthur vs Red Knight:
    arthur["hp"] = DuelArena.battle_knights(
        first_knight=arthur,
        second_knight=red_knight
    )
    red_knight["hp"] = DuelArena.battle_knights(
        first_knight=red_knight,
        second_knight=arthur
    )

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
