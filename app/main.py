from __future__ import annotations

from typing import Dict

from app.domain.builder import build_all
from app.services.combat import run_battle


def battle(knightsConfig: Dict[str, dict]) -> Dict[str, int]:
    knights = build_all(knightsConfig)
    return run_battle(knights)
