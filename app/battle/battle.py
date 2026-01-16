from app.classes.knight import Knight


def battle_fight(knight1: Knight, knight2: Knight) -> None:

    knight1.fight(knight2)
    knight2.fight(knight1)
