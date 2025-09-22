from __future__ import annotations

from typing import Dict, Tuple

from app.domain.models import Knight, Stats
from app.services.prebattle import prepare_stats


def _damage(attacker: Stats, defender: Stats) -> int:
    raw = attacker.power - defender.protection




def run_battle(
    knights: Dict[str, Knight],
) -> Dict[str, int]:
    prepared: Dict[str, Stats] = {
    }

    try:
    except KeyError as exc:
        raise KeyError(
            f"Missing required knight in config: {exc!s}"
        ) from exc


    return {
    }
