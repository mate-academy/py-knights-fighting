from app.models.knight import Knight
from app.services.compute_damage import compute_damage


def fight(attacker: Knight, defender: Knight) -> None:
    defender.current_hp = compute_damage(attacker, defender)
