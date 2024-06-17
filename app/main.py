from app.potion import Potion
from app.knight import Knight


def apply_equipment(knight: Knight) -> None:
    if knight.armour:
        for gear in knight.armour:
            knight.apply_armour(gear)
    if knight.weapon:
        knight.apply_weapon(knight.weapon)
    if knight.potion:
        knight.apply_potion(Potion(knight.potion))


def battle(knights_config: dict) -> dict:
    knights = {}
    for knight_info in knights_config.values():
        knight = Knight(**knight_info)
        apply_equipment(knight)
        knights[knight.name] = knight

    lancelot = knights.get("Lancelot")
    arthur = knights.get("Arthur")
    mordred = knights.get("Mordred")
    red_knight = knights.get("Red Knight")

    print("Round 1 \n"
          "Cruel battle between mighty Lancelot and cunning Mordred!")
    print("." * 15)
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    if lancelot.hp <= 0:
        lancelot.hp = 0
        print("Win for terrifying Mordred!")
        print("." * 15)

    if mordred.hp <= 0:
        mordred.hp = 0
        print("Win for glorious sir Lancelot!")

    print("Round 2 \n"
          "Exciting battle between king Arthur and mysterious Red Knight!")
    print("." * 15)

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection
    if arthur.hp <= 0:
        arthur.hp = 0
        print("Win for cryptic Red Knight!")

    if red_knight.hp <= 0:
        red_knight.hp = 0
        print("Win and glory for unbeatable king Arthur!")
    print("Tie!")
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
