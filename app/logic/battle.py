from app.models.knights import Knight


def apply_damage(attacker_power: int, defender: Knight) -> None:

    damage = attacker_power - defender.protection
    if damage < 0:
        damage = 0

    defender.hp -= damage
    if defender.hp < 0:
        defender.hp = 0


def battle_of_knights(knight1: Knight, knight2: Knight) -> None:

    p1_power = knight1.power
    p2_power = knight2.power

    apply_damage(p2_power, knight1)
    apply_damage(p1_power, knight2)
