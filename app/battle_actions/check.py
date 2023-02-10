from __future__ import annotations

from app.characters.knight import Knight


def check_hp(pair: list[Knight]) -> None:
    for knight in pair:
        if knight.hp < 0:
            knight.hp = 0
