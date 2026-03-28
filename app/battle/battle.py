from __future__ import annotations
from app.knight.knight import Knight


def duel(first_knight: Knight, second_knight: Knight) -> dict:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection
    first_knight.hp = check_if_fell(first_knight)
    second_knight.hp = check_if_fell(second_knight)
    return {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp
    }


def check_if_fell(knight: Knight) -> int:
    return knight.hp if knight.hp >= 0 else 0
