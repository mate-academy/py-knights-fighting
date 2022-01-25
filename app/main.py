from app.knight import Knight


def check_hp(knight):
    if knight.hp <= 0:
        knight.hp = 0


def duel(rival1, rival2):
    rival1.hp -= rival2.power - rival1.protection
    rival2.hp -= rival1.power - rival2.protection

    check_hp(rival1)
    check_hp(rival2)

    return rival1, rival2


def battle(knights):
    knights = {
        prsn["name"]: Knight(
            prsn["name"], prsn["power"], prsn["hp"],
            prsn["armour"], prsn["weapon"], prsn["potion"])
        for prsn in knights.values()
    }

    for knight in knights.values():
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion_if_any()

    duel(knights["Lancelot"], knights["Mordred"])
    duel(knights["Artur"], knights["Red Knight"])

    return {name: knight.hp for name, knight in knights.items()}
