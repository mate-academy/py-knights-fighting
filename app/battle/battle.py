from __future__ import annotations


def battle_versus(knight1: annotations, knight2: annotations) -> None:
    knight1.knight["hp"] -=\
        knight2.knight["power"] - knight1.knight["protection"]

    knight2.knight["hp"] -= \
        knight1.knight["power"] - knight2.knight["protection"]

    knights = [knight1, knight2]

    for knight in knights:
        if knight.knight["hp"] <= 0:
            knight.knight["hp"] = 0
