from __future__ import annotations


def battle_versus(hp: int | float,
                  power: int | float,
                  protection: int | float) -> int | float:
    hp -= power - protection
    if hp <= 0:
        return 0
    return hp
