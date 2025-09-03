from app.models.knight import Knight


def battle_between(knight1: Knight, knight2: Knight) -> dict:
    # Each knight attacks the other
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
