from app.character.knights import Knights


def attack(attacker: Knights, defender: Knights) -> None:
    attacker.hp -= defender.power - attacker.protection
    defender.hp -= attacker.power - defender.protection


def check_survival(character: Knights) -> None:
    if character.hp <= 0:
        character.hp = 0
