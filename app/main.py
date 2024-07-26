from app.characters.knights import KNIGHTS
from app.characters.knight import Knight

from app.characters.lancelot import lancelot
from app.characters.arthur import arthur
from app.characters.mordred import mordred
from app.characters.red_knight import red_knight

from app.characters.list_of_knight import list_of_knight


def battle(knights_config: list) -> None:
    # BATTLE PREPARATIONS:

    for knight in knights_config:
        knight.get_ready()

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


print(battle(list_of_knight))
