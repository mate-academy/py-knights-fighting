from app.camelot.knights import Knight


def take_damage(attacker: Knight, defender: Knight) -> int:
    dam = attacker.power - defender.protection
    return max(0, dam)


def attack(attacker: Knight, defender: Knight) -> None:
    damage = take_damage(attacker, defender)
    defender.hp -= damage

    if defender.hp <= 0:
        defender.hp = 0


def tournament(knight_1: Knight, knight_2: Knight) -> dict:
    attack(knight_1, knight_2)
    attack(knight_2, knight_1)

    return {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp
    }
