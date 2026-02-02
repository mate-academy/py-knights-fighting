from app.characters.knights import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    damage_1 = knight2.power - knight1.protection
    damage_2 = knight1.power - knight2.protection

    knight1.hp = max(0, knight1.hp - damage_1)
    knight2.hp = max(0, knight2.hp - damage_2)


def results(*knights: Knight) -> dict:
    return {k.name: k.hp for k in knights}
