from __future__ import annotations

from copy import deepcopy

from app.data.knights import KNIGHTS
from app.domain.types import BattleResult, KnightsConfig
from app.services.duel import duel_once
from app.services.preparation import prepare_knight


def battle(knights_config: KnightsConfig = KNIGHTS) -> BattleResult:
    knights_copy = deepcopy(knights_config)

    lancelot = prepare_knight(knights_copy["lancelot"])
    arthur = prepare_knight(knights_copy["arthur"])
    mordred = prepare_knight(knights_copy["mordred"])
    red_knight = prepare_knight(knights_copy["red_knight"])

    duel_once(lancelot, mordred)
    duel_once(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
