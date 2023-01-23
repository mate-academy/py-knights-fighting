from __future__ import annotations
from app.knights import make_instances


def battle(knight: dict) -> dict:
    all_knights = make_instances(knight)
    lancelot = 0
    mordred = 0
    artur = 0
    red_knight = 0
    for knights in all_knights:
        if knights.name == "Lancelot":
            lancelot = knights
        if knights.name == "Mordred":
            mordred = knights
        if knights.name == "Artur":
            artur = knights
        if knights.name == "Red Knight":
            red_knight = knights

    # battle lancelot vs mordred
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0
    if mordred.hp <= 0:
        mordred.hp = 0

    # battle artur vs red_knight
    artur.hp -= red_knight.power - artur.protection
    red_knight.hp -= artur.power - red_knight.protection

    # check if someone fell in battle
    if artur.hp <= 0:
        artur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        artur.name: artur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
