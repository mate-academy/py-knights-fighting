from __future__ import annotations
from app.buttle.models import Knight


def start_fight(pair_of_knights: list[Knight]) -> None:
    knight1, knight2 = pair_of_knights

    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    knight1.hp_checker()
    knight2.hp_checker()
