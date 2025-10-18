from app.data.knights import KNIGHTS
from app.fighter.fighter import Fighter


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    lancelot = Fighter(knights_config["lancelot"])
    arthur = Fighter(knights_config["arthur"])
    mordred = Fighter(knights_config["mordred"])
    red_knight = Fighter(knights_config["red_knight"])

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in fighter
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in fighter
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return fighter results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
