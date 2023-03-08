from app.knights.knight_dict import knights
from app.knights.knight import CamelotKnights


def battle(knights: dict) -> dict:
    for i in knights:
        knights[i] = CamelotKnights(
            name=knights[i]["name"],
            power=knights[i]["power"],
            hp=knights[i]["hp"],
            armour=knights[i]["armour"],
            weapon=knights[i]["weapon"],
            potion=knights[i]["potion"]
        )
        knights[i].battle_preparation()

    lanc = knights["lancelot"]
    morde = knights["mordred"]
    arte = knights["arthur"]
    red_k = knights["red_knight"]

    lanc.hp -= morde.power - lanc.protection
    morde.hp -= lanc.power - morde.protection

    if lanc.hp <= 0:
        lanc.hp = 0

    if morde.hp <= 0:
        morde.hp = 0

    arte.hp -= red_k.power - arte.protection
    red_k.hp -= arte.power - red_k.protection

    if arte.hp <= 0:
        arte.hp = 0

    if red_k.hp <= 0:
        red_k.hp = 0

    return {
        lanc.name: lanc.hp,
        arte.name: arte.hp,
        morde.name: morde.hp,
        red_k.name: red_k.hp,
    }


print(battle(knights))
