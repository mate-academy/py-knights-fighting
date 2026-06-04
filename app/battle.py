from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.knight import KnightConfig


def fight(first_knight: KnightConfig, second_knight: KnightConfig) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection
    hp_check(first_knight)
    hp_check(second_knight)


def hp_check(battle_warrior: KnightConfig) -> None:
    if battle_warrior.hp <= 0:
        battle_warrior.hp = 0
