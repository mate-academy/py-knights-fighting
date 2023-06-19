from app.knights.knight import Knights


def winner(knight_1: Knights, knight_2: Knights) -> Knights:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection
    if knight_1.hp <= 0:
        knight_1.hp = 0
        return knight_1
    if knight_2.hp <= 0:
        knight_2.hp = 0
        return knight_2


def battle(knights: dict) -> dict:
    for elem in knights:
        knights[elem] = Knights(**knights[elem])

    lanc = knights["lancelot"]
    morde = knights["mordred"]
    arte = knights["arthur"]
    red_k = knights["red_knight"]

    winner(lanc, morde)
    winner(arte, red_k)

    return {
        lanc.name: lanc.hp,
        arte.name: arte.hp,
        morde.name: morde.hp,
        red_k.name: red_k.hp,
    }
