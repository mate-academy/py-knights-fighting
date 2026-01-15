from app.character.knight import Knight


def attack(attacker: Knight, defender: Knight) -> None:
    attacker.hp -= defender.power - attacker.protection
    defender.hp -= attacker.power - defender.protection


def check_survival(character: Knight) -> None:
    if character.hp <= 0:
        character.hp = 0
