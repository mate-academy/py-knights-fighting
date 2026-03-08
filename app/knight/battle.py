from typing import Dict
from app.knight.models import Knight
from app.knight.services import prepare_knight


def fight(knight_a: Knight, knight_b: Knight) -> Dict[str, int]:
    prepare_knight(knight_a)
    prepare_knight(knight_b)

    knight_a.take_damage(max(0, knight_b.power - knight_a.protection))
    knight_b.take_damage(max(0, knight_a.power - knight_b.protection))

    return {knight_a.name: knight_a.hp, knight_b.name: knight_b.hp}
