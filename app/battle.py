from app.knights import formation_knight, Knight


def battle_pre(knight1: Knight, knight2: Knight) -> dict:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_dict: dict) -> dict:
    lancelot = formation_knight(knights_dict["lancelot"])
    arthur = formation_knight(knights_dict["arthur"])
    mordred = formation_knight(knights_dict["mordred"])
    red_knight = formation_knight(knights_dict["red_knight"])

    battle_pre(lancelot, mordred)
    battle_pre(arthur, red_knight)
    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}
