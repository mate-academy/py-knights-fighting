from __future__ import annotations
from app.buttle.preparations_classes import Knight


def start_fight(pair_of_knights: list[Knight]) -> None:
    knight1, knight2 = pair_of_knights

    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    # check if someone fell in battle
    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0
