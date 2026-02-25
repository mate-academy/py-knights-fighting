from app.models import Knight


def conduct_duel(attacker: Knight, defender: Knight) -> None:
    """Лицарі б'ють один одного одночасно."""
    power_a = attacker.power
    power_b = defender.power

    attacker.receive_damage(power_b)
    defender.receive_damage(power_a)
