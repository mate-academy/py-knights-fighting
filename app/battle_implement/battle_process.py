from __future__ import annotations

from app.entities.knight import Knight


def battle_process(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.battle_preparation()
    second_knight.battle_preparation()
    first_knight - second_knight
    first_knight.is_defeated()
    second_knight.is_defeated()


def battles_result(knights: dict) -> dict:
    return {knight.name: knight.hp for knight in knights.values()}
