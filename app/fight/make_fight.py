from __future__ import annotations
from app.participants.create_knights import Knight


def correct_damage(defend: Knight, attack: Knight) -> int:  # TODO remove to class method
    damage = max(0, attack.power - defend.protection)
    defend.hp = max(0, defend.hp - damage)
    return defend.hp


def get_fight_result(pairs: list, table: dict) -> dict:
    for pair in pairs:
        op1, op2 = pair
        table[op1.display_name] = correct_damage(op1, op2)
        table[op2.display_name] = correct_damage(op2, op1)

    return table
