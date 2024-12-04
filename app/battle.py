from __future__ import annotations
from app.preparations.knight import Knight


def battle_between_two_knights(knight_one: Knight, knight_two: Knight) -> None:
    knight_one.calculate_hp_after_damage(knight_two.power)
    knight_two.calculate_hp_after_damage(knight_one.power)


def battle_results(knights_dict: dict) -> dict:
    return {knight.name: knight.hp for knight in knights_dict.values()}
