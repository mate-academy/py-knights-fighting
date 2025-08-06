from app.models.knight import Knight


def battle(knight1: Knight, knight2: Knight) -> dict[str, int]:
    knight1.apply_equipment()
    knight2.apply_equipment()

    damage_to_1 = max(knight2.power - knight1.protection, 0)
    damage_to_2 = max(knight1.power - knight2.protection, 0)

    knight1.receive_damage(damage_to_1)
    knight2.receive_damage(damage_to_2)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }
