"""Battle resolution logic for the Camelot tournament."""

from __future__ import annotations

from typing import Any

from app.knight import Knight


def resolve_round(first_knight: Knight, second_knight: Knight) -> None:
    """Resolve one simultaneous exchange between two knights."""
    first_damage = second_knight.power - first_knight.protection
    second_damage = first_knight.power - second_knight.protection

    first_knight.hp = max(
        0,
        first_knight.hp - first_damage,
    )
    second_knight.hp = max(
        0,
        second_knight.hp - second_damage,
    )


def simulate_battle(
    knights_config: dict[str, dict[str, Any]],
) -> dict[str, int]:
    """Calculate the outcome of the scheduled battle matches."""
    knights = {
        name: Knight.from_config(raw_knight)
        for name, raw_knight in knights_config.items()
    }

    pairings = (
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    )

    for first_name, second_name in pairings:
        if first_name in knights and second_name in knights:
            resolve_round(knights[first_name], knights[second_name])

    return {knight.name: knight.hp for knight in knights.values()}
