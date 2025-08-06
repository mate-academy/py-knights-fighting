from app.models.knight import Knight  # якщо клас Knight у цьому модулі


def battle(knight1: Knight, knight2: Knight) -> Knight:
    damage_to_1 = max(0, knight2.power - knight1.protection)
    damage_to_2 = max(0, knight1.power - knight2.protection)

    knight1.receive_damage(damage_to_1)
    knight2.receive_damage(damage_to_2)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
