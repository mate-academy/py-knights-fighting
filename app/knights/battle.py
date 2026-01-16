from app.knights.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    """Simulate one round of fight between two knights."""
    knight1.attack(knight2)
    knight2.attack(knight1)
