from app.KNIGHTS.KnightsInfo import KNIGHTS
from app.KNIGHTS.ReformattingInfo import making_knight


def battle(knights_config: dict) -> dict:
    # Reformatting info about the Knights

    # lancelot

    lancelot = making_knight(knights_config["lancelot"])

    # arthur
    arthur = making_knight(knights_config["arthur"])

    # mordred

    mordred = making_knight(knights_config["mordred"])

    # red_knight

    red_knight = making_knight(knights_config["red_knight"])

    knights_list = [lancelot, arthur, mordred, red_knight]

# BATTLE------------------------------------------------

    # 1 Lancelot vs Mordred:

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # 2 Arthur vs Red Knight:

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle

    for knight in knights_list:
        if knight.hp <= 0:
            knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
