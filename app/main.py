from app.knights import KNIGHTS
from app.preparation import Knight


def create_knights(attributes: dict) -> list:
    knights = []
    for attributes in attributes.values():
        knights.append(Knight(name=attributes["name"],
                              power=attributes["power"],
                              hp=attributes["hp"],
                              armour=attributes["armour"],
                              weapon=attributes["weapon"],
                              potion=attributes["potion"]))
    for knight in knights:
        knight.preparation()
    return knights


def check_hp(knight):
    if knight.hp <= 0:
        knight.hp = 0

def fight(knight1, knight2):
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    check_hp(knight1)
    check_hp(knight2)


def battle(knights: dict):
    knights = create_knights(knights)
    fight(knights[0], knights[2])
    fight(knights[1], knights[3])

    return {
        knights[0].name: knights[0].hp,
        knights[1].name: knights[1].hp,
        knights[2].name: knights[2].hp,
        knights[3].name: knights[3].hp
    }


print(battle(KNIGHTS))
