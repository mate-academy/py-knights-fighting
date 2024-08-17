from app.preparations.knights import create_knights
from app.preparations.buffs import apply_buffs
from app.fighting.fight import start_fight
from app.fighting.result import check_fight_result


def battle(knight_config: dict) -> dict:
    # PREPARATIONS
    knights = create_knights(knight_config)
    apply_buffs(knights)

    # FIGHT
    start_fight(knights)

    # CHECK RESULTS
    result = check_fight_result(knights)

    return result
