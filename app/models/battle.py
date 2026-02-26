from app.models.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> dict:
    damage_to_knight1 = max(knight2.power - knight1.protection, 0)
    knight1.hp -= damage_to_knight1

    damage_to_knight2 = max(knight1.power - knight2.protection, 0)
    knight2.hp -= damage_to_knight2

    result = {
        knight1.name: max(knight1.hp, 0),
        knight2.name: max(knight2.hp, 0),
    }
    return result
