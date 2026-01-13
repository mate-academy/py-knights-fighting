from app.battle import battle
from app.knights_config import KNIGHTS


def run_battle() -> dict:
    return battle(KNIGHTS)
