from app.fighters.knight import Knight


def init_knights(knights: dict) -> dict:
    battle_participants = {}
    for knight in knights.values():
        new_knight = Knight(knight)
        battle_participants[new_knight.name.lower()] = new_knight
    return battle_participants


def fight(knight1: Knight, knight2: Knight) -> dict:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }


def battle(knights_characteristics: dict) -> dict:
    fighters = init_knights(knights_characteristics)
    lancelot = fighters["lancelot"]
    mordred = fighters["mordred"]
    red_knight = fighters["red knight"]
    arthur = fighters["arthur"]

    round1 = fight(lancelot, mordred)
    round2 = fight(red_knight, arthur)
    return {**round1, **round2}
