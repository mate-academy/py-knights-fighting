from __future__ import annotations
from app.services.config import prepare_models
from app.services.fight import duel


def battle(knights_config: dict) -> dict:
    models = prepare_models(knights_config)
    return duel(models)
