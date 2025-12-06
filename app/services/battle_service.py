from app.models.knight import Knight


def duel(k1: Knight, k2: Knight) -> None:
    """Simultaneous exchange of damage."""
    k1.take_damage(k2.power - k1.protection)
    k2.take_damage(k1.power - k2.protection)


def prepare_knights(knights_config) -> dict:
    """Convert dict config into Knight objects with applied effects."""
    knights = {k: Knight(conf) for k, conf in knights_config.items()}
    for knight in knights.values():
        knight.prepare()
    return knights
