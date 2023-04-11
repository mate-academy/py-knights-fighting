from typing import List

from app.knight import Knight


def fight(knights: List[Knight]) -> None:
    i = 1

    for knight in knights:
        knight.hp -= knights[i].power - knight.protection
        if knight.hp <= 0:
            knight.hp = 0
        i -= 1
