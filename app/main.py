from app.KNIGHTS.KnightsInfo import KNIGHTS
from app.KNIGHTS.ReformattingInfo import making_knight


def battle(knights_config: dict) -> None:
    # Reformatting info about the Knights

    # lancelot
    lancelot = knights_config["lancelot"]

    lancelot = making_knight(lancelot)

    # arthur
    arthur = knights_config["arthur"]

    arthur = making_knight(arthur)

    # mordred
    mordred = knights_config["mordred"]

    mordred = making_knight(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]

    red_knight = making_knight(red_knight)

# BATTLE------------------------------------------------

    # 1 Lancelot vs Mordred:

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # 2 Arthur vs Red Knight:

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle

    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
