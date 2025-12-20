from app.models.knight import Knight
from app.services.compute_damage import compute_damage


def duel(knight_a: Knight, knight_b: Knight) -> None:
    damage_to_b = compute_damage(knight_a, knight_b)
    damage_to_a = compute_damage(knight_b, knight_a)

    knight_b.take_damage(damage_to_b)
    knight_a.take_damage(damage_to_a)
