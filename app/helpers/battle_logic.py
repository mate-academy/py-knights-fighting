from app.models.knight import Knight


def fight(attacker: Knight, defender: Knight) -> None:
    damage = attacker.power - defender.protection
    if damage > 0:
        defender.hp -= damage

    if defender.hp < 0:
        defender.hp = 0
