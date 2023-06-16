from app.preparation import Knight


def create_knights(attributes: dict) -> dict:
    knights = {}
    for attr in attributes.values():
        knight = Knight(
            name=attr["name"],
            power=attr["power"],
            hp=attr["hp"],
            armour=attr["armour"],
            weapon=attr["weapon"],
            potion=attr["potion"]
        )
        knight.preparation()
        knights[knight.name] = knight
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
    fight(knights["Lancelot"], knights["Mordred"])
    fight(knights["Artur"], knights["Red Knight"])

    return {knight.name: knight.hp for knight in knights.values()}
