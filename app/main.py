from app.modules.knights import Knight


def battle(knights_dict: dict) -> dict:
    result_dict = {}

    Knight.make_knight(knights_dict)
    knight = Knight.knights

    knight1 = knight["Lancelot"]
    knight2 = knight["Arthur"]
    knight3 = knight["Mordred"]
    knight4 = knight["Red Knight"]

    knight1.hp -= knight3.power - knight1.protection
    knight3.hp -= knight1.power - knight3.protection
    knight2.hp -= knight4.power - knight2.protection
    knight4.hp -= knight2.power - knight4.protection

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0

    if knight3.hp <= 0:
        knight3.hp = 0

    if knight4.hp <= 0:
        knight4.hp = 0

    result_dict.update({
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
        knight3.name: knight3.hp,
        knight4.name: knight4.hp
    })

    return result_dict
