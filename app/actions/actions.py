from __future__ import annotations

from app.characters.knight import Knight
from typing import List


def check_hp(knight: Knight) -> None:
    if knight.hp < 0:
        knight.hp = 0


def duel(duel_participants: List[Knight]) -> None:
    first_knight = duel_participants[0]
    second_knight = duel_participants[1]

    first_knight.attack(second_knight)
    second_knight.attack(first_knight)
