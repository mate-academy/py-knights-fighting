from __future__ import annotations

from typing import Dict, Tuple

from app.domain.models import Knight, Stats
from app.services.prebattle import prepare_stats


def _damage(attacker: Stats, defender: Stats) -> int:
    raw = attacker.power - defender.protection
    return raw if raw > 0 else 0


def duel(
    first: Stats, second: Stats
) -> Tuple[Stats, Stats]:
    first.hp -= _damage(second, first)
    second.hp -= _damage(first, second)
    if first.hp < 0:
        first.hp = 0
    if second.hp < 0:
        second.hp = 0
    return first, second


def run_battle(
    knights: Dict[str, Knight],
) -> Dict[str, int]:
    prepared: Dict[str, Stats] = {
        key: prepare_stats(value)
        for key, value in knights.items()
    }

    try:
        stats_lancelot = prepared["lancelot"]
        stats_mordred = prepared["mordred"]
        stats_arthur = prepared["arthur"]
        stats_red_knight = prepared["red_knight"]
    except KeyError as exc:
        raise KeyError(
            f"Missing required knight in config: {exc!s}"
        ) from exc

    duel(stats_lancelot, stats_mordred)
    duel(stats_arthur, stats_red_knight)

    return {
        stats_lancelot.name: stats_lancelot.hp,
        stats_arthur.name: stats_arthur.hp,
        stats_mordred.name: stats_mordred.hp,
        stats_red_knight.name: stats_red_knight.hp,
    }
