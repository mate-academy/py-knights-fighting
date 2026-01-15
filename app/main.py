from app.knights.configs import KNIGHTS
from app.battle_arena.battle_arena_obj import Arena


def battle(knights_config: dict) -> dict:
    arena = Arena()
    arena.knight_registration(knights_config)

    arena.fighting(
        arena.knights.get("lancelot"),
        arena.knights.get("mordred")
    )

    arena.fighting(
        arena.knights.get("arthur"),
        arena.knights.get("red_knight")
    )

    return arena.battle_results


print(battle(KNIGHTS))
