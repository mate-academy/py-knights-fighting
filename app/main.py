from app.data.knights_data import KNIGHTS
from app.knight import Knight


# TODO: refactor battle() method and move to separate module
def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight.create_knight(knights_config["lancelot"])
    lancelot.prepare_for_battle()

    # arthur
    arthur = Knight.create_knight(knights_config["arthur"])
    arthur.prepare_for_battle()

    # mordred
    mordred = Knight.create_knight(knights_config["mordred"])
    mordred.prepare_for_battle()

    # red_knight
    red_knight = Knight.create_knight(knights_config["red_knight"])
    red_knight.prepare_for_battle()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
