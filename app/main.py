from app.knights.knights_data import KNIGHTS
from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {name: Knight(**config) for name,
               config in knights_config.items()}

    # lancelot
    lancelot = knights["lancelot"]

    # arthur
    arthur = knights["arthur"]

    # mordred
    mordred = knights["mordred"]

    # red_knight
    red_knight = knights["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle

    for knight in knights.values():
        if knight.hp <= 0:
            knight.hp = 0
    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
