from app.Service.organizer import knights


def let_fight_begin() -> dict:
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot.hp -= mordred.pwr - lancelot.ptn
    mordred.hp -= lancelot.pwr - mordred.ptn

    arthur.hp -= red_knight.pwr - arthur.ptn
    red_knight.hp -= arthur.pwr - red_knight.ptn

    for knight in knights:
        if knights[f"{knight}"].hp <= 0:
            knights[f"{knight}"].hp = 0

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }
