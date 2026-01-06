from app.models import Knight


def resolve_duel(attacker: Knight, defender: Knight) -> tuple[int, int]:
    attacker_hp = max(
        0,
        attacker.hp - (defender.power - attacker.protection),
    )
    defender_hp = max(
        0,
        defender.hp - (attacker.power - defender.protection),
    )
    return attacker_hp, defender_hp
