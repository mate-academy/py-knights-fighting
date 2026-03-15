from app.knights.builder import build_knights_from_config
from app.combat.battle import battle as compute_battle
from app.config import KNIGHTS as DEFAULT_KNIGHTS


def battle(knights_config: dict = None) -> dict:
    config = knights_config or DEFAULT_KNIGHTS
    knights = build_knights_from_config(config)
    lancelot = knights.get("lancelot")
    mordred = knights.get("mordred")
    arthur = knights.get("arthur")
    red = knights.get("red_knight")
    result_1 = compute_battle(lancelot, mordred)
    result_2 = compute_battle(arthur, red)

    return {**result_1, **result_2}
