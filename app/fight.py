from typing import List

from app.knight import Knight


def fight(knights: List[Knight]):
    for count, knight in enumerate(knights):
        knight.hp += knight.protection

        if count == 0:
            knight.hp -= knights[count + 1].power
        else:
            knight.hp -= knights[count - 1].power

        if knight.hp <= 0:
            knight.hp = 0
