from app.knights.models import Knight


def fight(knight1: Knight, knight2: Knight) -> tuple[Knight, Knight]:
    damage_to_1 = max(knight2.power - knight1.protection, 0)
    damage_to_2 = max(knight1.power - knight2.protection, 0)

    knight1.take_damage(damage_to_1)
    knight2.take_damage(damage_to_2)

    return knight1, knight2


def battle(knight1: Knight, knight2: Knight) -> dict[str, int]:
    knight1, knight2 = fight(knight1, knight2)
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
