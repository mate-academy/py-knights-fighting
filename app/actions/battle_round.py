from __future__ import annotations

from app.knights.battle_preparations import Knight


def battle_round(knights: dict) -> dict:
    battle(knights["Lancelot"], knights["Mordred"])
    battle(knights["Artur"], knights["Red Knight"])

    return knights


def battle(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection
