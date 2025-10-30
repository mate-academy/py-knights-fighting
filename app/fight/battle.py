from app.knights.knight import Knight


def calculate_damage(attacker_power: int, defender_protection: int) -> int:

    damage = attacker_power - defender_protection
    return max(0, damage)


def conduct_battle(knight1: Knight, knight2: Knight) -> None:

    # Damage calculation requires calling the @property attributes
    # (assuming they are implemented correctly in Knight class).

    damage_to_1 = calculate_damage(
        attacker_power=knight2.effective_power,
        defender_protection=knight1.protection
    )

    damage_to_2 = calculate_damage(
        attacker_power=knight1.effective_power,
        defender_protection=knight2.protection
    )

    knight1.take_damage(damage_to_1)
    knight2.take_damage(damage_to_2)
