from typing import Any, Dict

from app.battle.arena import run_battle
from app.config import BATTLE_PAIRS, KNIGHTS


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    return run_battle(knights_config, BATTLE_PAIRS)


if __name__ == "__main__":
    print(battle(KNIGHTS))
