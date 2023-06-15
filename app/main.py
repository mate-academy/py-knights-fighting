from app.preparation import Knight


def create_knights(attributes: dict) -> list:
    knights = []
    for attr in attributes.values():
        knight = Knight(name=attr["name"],
                        power=attr["power"],
                        hp=attr["hp"],
                        armour=attr["armour"],
                        weapon=attr["weapon"],
                        potion=attr["potion"])
        knight.preparation()
        knights.append(knight)
    return knights


def check_hp(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    check_hp(knight1)
    check_hp(knight2)


def battle(knights: dict) -> dict:
    knights = create_knights(knights)
    fight(knights[0], knights[2])
    fight(knights[1], knights[3])

    return {
        knights[0].name: knights[0].hp,
        knights[1].name: knights[1].hp,
        knights[2].name: knights[2].hp,
        knights[3].name: knights[3].hp
    }
