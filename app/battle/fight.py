from __future__ import annotations
from app.classes.class_knights import Knights


def fight_vs(knight1: Knights, knight2: Knights) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    knight1.hp = 0 if knight1.hp < 0 else knight1.hp
    knight2.hp = 0 if knight2.hp < 0 else knight2.hp
