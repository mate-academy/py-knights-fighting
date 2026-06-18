from typing import Dict

from app.battle import run_battle
from app.config import KNIGHTS


def battle(knights_config: dict) -> Dict[str, int]:
    return run_battle(knights_config)


if __name__ == "__main__":
    print(battle(KNIGHTS))
