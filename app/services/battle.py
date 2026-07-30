from app.models.knight import Knight


def conduct_battle(knight1: Knight, knight2: Knight) -> None:
    knight1.fight(knight2)
    knight2.fight(knight1)
