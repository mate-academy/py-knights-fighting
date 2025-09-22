from __future__ import annotations

from typing import Dict

from app.domain.builder import build_all
from app.services.combat import run_battle


def battle(
    knights_config: Dict[str, dict],
) -> Dict[str, int]:
    knights = build_all(knights_config)
    return run_battle(knights)


if __name__ == "__main__":
    print()
