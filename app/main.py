from app.preparations.knights import create_knights
from app.preparations.buffs import apply_buffs
from app.fighting.fight import start_fight
from app.fighting.result import check_fight_result


def battle(knight_config: dict) -> dict:
    knights = create_knights(knight_config)
    apply_buffs(knights)

    start_fight(knights)

    result = check_fight_result(knights)

    return result
