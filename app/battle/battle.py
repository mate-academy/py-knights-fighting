from __future__ import annotations
from app.knights.knight_prototype import Knight


def battle_preparation(knight: Knight) -> None:
    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()


def battle_between_knights(
        first_knight: Knight,
        second_knight: Knight
) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection


def fallen(knights: list[Knight]) -> None:
    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0
