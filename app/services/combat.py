from __future__ import annotations

from typing import Dict, Tuple

from app.domain.models import Knight, Stats
from app.services.prebattle import prepare_stats


def _damage(attacker: Stats, defender: Stats) -> int:
    raw = attacker.power - defender.protection
    return (
        raw if raw > 0 else 0
    )  # zabezpiecza przed „leczeniem”


def duel(a: Stats, b: Stats) -> Tuple[Stats, Stats]:
    a.hp -= _damage(b, a)
    b.hp -= _damage(a, b)
    if a.hp < 0:
        a.hp = 0
    if b.hp < 0:
        b.hp = 0
    return a, b


def run_battle(
    knights: Dict[str, Knight],
) -> Dict[str, int]:
    prepared: Dict[str, Stats] = {
        k: prepare_stats(v) for k, v in knights.items()
    }

    try:
        lancelot_ = prepared["lancelot"]
        m = prepared["mordred"]
        a = prepared["arthur"]
        r = prepared["red_knight"]
    except KeyError as exc:
        raise KeyError(
            f"Missing required knight in config: {exc!s}"
        ) from exc

    duel(lancelot_, m)
    duel(a, r)

    return {
        lancelot_.name: lancelot_.hp,
        a.name: a.hp,
        m.name: m.hp,
        r.name: r.hp,
    }
