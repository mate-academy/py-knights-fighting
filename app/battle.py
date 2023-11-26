from app.knights import Knight


def battle(knight1: Knight, knight2: Knight) -> None:
    apply_damage(knight1, knight2)
    apply_damage(knight2, knight1)


def apply_damage(attacker: Knight, defender: Knight) -> None:
    damage = max(0, attacker.power - defender.protection)
    defender.hp = max(defender.hp - damage, 0)
