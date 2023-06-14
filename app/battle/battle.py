from app.battle.preparation import Preparation


def battle_versus(knight1: Preparation, knight2: Preparation) -> None:
    knight1.knight["hp"] -= (
            knight2.knight["power"] - knight1.knight["protection"]
    )

    knight2.knight["hp"] -= (
            knight1.knight["power"] - knight2.knight["protection"]
    )

    knights = [knight1, knight2]

    for knight in knights:
        if knight.knight["hp"] <= 0:
            knight.knight["hp"] = 0
