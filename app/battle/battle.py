from app.classes.knight import Knight


def battle_fight(knight1: Knight, knight2: Knight) -> None:

    knight1.ready_for_battle()
    knight2.ready_for_battle()

    knight1.fight(knight2)
    knight2.fight(knight1)
