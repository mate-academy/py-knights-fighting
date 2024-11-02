from app.knights.knight import Knight


def calculate_damage(attacker: Knight, defender: Knight) -> int:
    return max(
        0,
        attacker.stats["power"] - defender.stats["protection"]
    )


def fight(knight1: Knight, knight2: Knight) -> dict:
    # Knight 1 attacks Knight 2
    damage_to_knight2 = calculate_damage(knight1, knight2)
    knight2.receive_damage(damage_to_knight2)

    # Knight 2 attacks Knight 1
    damage_to_knight1 = calculate_damage(knight2, knight1)
    knight1.receive_damage(damage_to_knight1)

    return {
        knight1.name: knight1.stats["hp"],
        knight2.name: knight2.stats["hp"]
    }
