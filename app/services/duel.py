from __future__ import annotations

from app.domain.types import KnightStats


def duel_once(left: KnightStats, right: KnightStats) -> None:
    left_hp_before = left["hp"]
    right_hp_before = right["hp"]
    left_damage = max(0, right["power"] - left["protection"])
    right_damage = max(0, left["power"] - right["protection"])

    left["hp"] = left_hp_before - left_damage
    right["hp"] = right_hp_before - right_damage

    if left["hp"] <= 0:
        left["hp"] = 0
    if right["hp"] <= 0:
        right["hp"] = 0
